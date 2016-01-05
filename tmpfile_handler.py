import os
import redis
import sys
import multiprocessing
import json
import time


import util
import config

class Tmpfile_hander(object):
    def __init__(self , logger = None, **redis_kwargs) :
        self.logger = logger
        self.rd = redis.Redis(**redis_kwargs)
        # self.processes = []
        self.lock = multiprocessing.RLock()
        self.processes = []

    def push_message(self, out_json_message):
        next_queue = out_json_message['next_queue']
        del out_json_message['next_queue']
        return self.rd.lpush(next_queue, json.dumps(out_json_message))

    def prepare_args(self, args_str):
        try:
            args = json.loads(args_str)
        except (TypeError, ValueError):
            util.write_log_error(self.lock, self.logger, 'can not parse %s to json args.'%(args_str))
            return None
        if not 'file_name' in args:
            util.write_log_error(self.lock, self.logger, 'file_name not found.')
            return None
        if not 'level' in args:
            args['level'] = 'low'
        if not 'target_folder' in args:
            args['target_folder'] = config.DEFAULT_FILE_HANDLE_FOLDER
        if not 'message_type' in args:
            args['message_type'] = config.MESSAGE_TYPE_NORMAL
        download_time = float(os.path.splitext(os.path.basename(args['file_name']))[0].split('_')[1])
        args['download_time'] = time.strftime('%Y-%m-%d/%H:%M:%S',time.localtime(download_time))
        return args

    def prepare_apk_info(self, args):
        apk_info={}
        for info in ['source','category','download_count','upload_time','rating','download_redirect_urls','detail_url','download_time','app_name', 'otherinfo']:
            if info in args:
                if info == 'download_redirect_urls':
                    apk_info['download_urls'] = args[info]
                elif info == 'app_name':
                    apk_info['name'] = args[info]
                else:
                    apk_info[info] = args[info]
        return apk_info

    def crawl(self, args):
        file_name = args['file_name']
        target_folder = args['target_folder']
        apk_info = self.prepare_apk_info(args)
        util.makeDirs(self.lock, target_folder)
        if not util.verify_apk(file_name):
            util.write_log_warn(self.lock, self.logger, "FAILED :  %s jarsigner faild."%(file_name))
            os.remove(file_name)
            return False
        md5 = util.get_file_MD5(file_name)
        apk_info['MD5'] = md5
        target_name = target_folder + 'cell-' + md5[:2] + '/' + md5 + '.apk'
        if os.path.exists(target_name):
            os.remove(file_name)
        else:
            apk_info['new'] = 'True'
            os.rename(args['file_name'], target_name)
        util.writeApkInfoFile(self.lock, target_folder,apk_info)
        util.writeRecord(self.lock, target_folder,apk_info)
        util.write_log_info(self.lock, self.logger, "SUCCESS : %s handle success"%(args['file_name']))
        return True

    def normal(self, args):
        util.write_log_warn(self.lock, self.logger, '"normal" message type did nothing.')
        return True

    def do_work(self, message):
        args = self.prepare_args(message)
        if args is None:
            return
        return eval('self.'+args['message_type'])(args)

    def work_process(self):
        util.write_log_info(self.lock, self.logger, 'new tmpfile_hander process started')
        while 1:
            try:
                message = self.rd.brpop([config.HIGH_FILE_HANDLE_QUEUE, config.LOW_FILE_HANDLE_QUEUE],0)
                util.write_log_info(self.lock, self.logger, 'received new nessage: %s'%(message[1]))
                self.do_work(message[1])
            except Exception:
                import traceback
                util.write_log_error(self.lock, self.logger,"tmpfile_hander process catched exception." + traceback.print_exc())

    def launch(self):
        for i in xrange(config.MAX_FILEHANDLE_PROCESS_NUM):
            process = multiprocessing.Process(name = 'tmpfile_hander_process_'+ `i`, target = self.work_process)
            process.daemon = True
            self.processes.append(process)
            process.start()

    def quit(self):
        self.rd.save()
        for process in self.processes:
            process.terminate()
            process.join()
        sys.exit(-1)
##########################################################################################
def main(argv):
    logger = None
    if config.LOGGER_ENABLED:
        logger = util.initLog(config.LOGGER_NAME_FILE_HANDLER)
    multiprocessing.current_process().name = 'tmpfile_hander_process_main'
    tmpfile_hander = Tmpfile_hander(logger = logger, host = config.REDIS_HOST, port = config.REDIS_PORT)
    util.write_log_info(tmpfile_hander.lock, tmpfile_hander.logger,"[+]start tmpfile_hander...")
    tmpfile_hander.launch()
    try:
        content=raw_input()
        while content != 'exit':
            content=raw_input()
    except KeyboardInterrupt:
        pass
    util.write_log_info(tmpfile_hander.lock, tmpfile_hander.logger,"user determined tmpfile_hander")
    tmpfile_hander.quit()

if __name__ == '__main__':
    main(sys.argv)