# -*- coding: utf-8 -*-
import os
from subprocess import Popen,PIPE
import hashlib
import json
import threading
import logging
import logging.handlers
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import selenium.common.exceptions as selenium_exception
import random
# import codecs

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import config

def start_phantomJS_browser():
    try:
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] =config.PHANTOMJS_USER_AGENT
        phantomJS_browser = webdriver.PhantomJS(desired_capabilities=dcap, service_log_path=os.path.devnull)
        phantomJS_browser.implicitly_wait(config.IMPLICITLY_WAIT_TIME)
        phantomJS_browser.set_page_load_timeout(config.PAGE_LOAD_TIMEOUT)
        phantomJS_browser.set_script_timeout(config.SCRIPT_TIMEOUT)
    except Exception:
        return None
    return phantomJS_browser

def dec2hex(string_num):
    base = [str(x) for x in range(10)] + [ chr(x) for x in range(ord('a'),ord('a')+6)]
    num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num,rem = divmod(num, 16)
        mid.append(base[rem])
    return ''.join([str(x) for x in mid[::-1]])

#构造目录结构
def makeDirs(lock, basepath):
    if os.path.exists(basepath+'/cell-00'):
        return
    with lock:
        for i in range(1,256):
            if i<16:
                str_hex = "cell-0"+dec2hex(str(i))
            else:
                str_hex = "cell-"+dec2hex(str(i))
            os.mkdir(basepath+'/'+str_hex)
        os.mkdir(basepath+'/cell-00')

def initLog(handler):
    if not os.path.exists('log'):
        os.mkdir('log')
    #Log日志
    logger = logging.getLogger(handler)
    #set loghandler  
    fileh = logging.handlers.RotatingFileHandler('log/'+handler,'a',10*1024*1024,5) 
    consoleh =  logging.StreamHandler()
    logger.addHandler(fileh)
    logger.addHandler(consoleh)
    #set formater  
    formatter = logging.Formatter(config.LOGGER_FORMATTER)  
    fileh.setFormatter(formatter)
    consoleh.setFormatter(formatter)   
    #set log level
    consoleh.setLevel(config.CONSOLE_LOGGER_LEVEL)
    fileh.setLevel(config.FILE_LOGGER_LEVEL)
    logger.setLevel(config.LOGGER_LEVEL)
    return logger


#获取文件的MD5值
def get_file_MD5(filepath):
    f = open(filepath,'rb')
    hash = get_MD5(f.read())
    f.close()
    return hash

#md5 of string(generally url)
def get_MD5(s):
    md5obj = hashlib.md5()
    md5obj.update(s)
    hash = md5obj.hexdigest()
    return hash

#调用控制台命令
def exec_cmd(cmd_str, check_returncode=True, log=True):
    if log:
        ctime = strftime("%Y_%m_%d_%H_%M_%S", gmtime())
        dev_logfp.write("\n [{0}]: \t {1} \n ".format(ctime, cmd_str))
        p = Popen(cmd_str.split(), stderr=dev_logfp, stdout=dev_logfp)
        # dev_logfp.flush()
    else:
        p = Popen(cmd_str.split(), stderr=PIPE, stdout=PIPE)

    output, errors = p.communicate()

    if check_returncode and p.returncode != 0:
        msg = "'{0}' return code '{1}' ".format(cmd_str, p.returncode)
        print msg

    return [p.returncode, output, errors]

#通过jarsigner校验apk
def verify_apk(apk_path):
    cmd_str = 'jarsigner -verify '+apk_path
    [ret_code,output,errors] = exec_cmd(cmd_str,log = False)
    check_arg = u'jar 已验证'
    for line in output.splitlines():        
        if check_arg in line:
            return True
    return False

def make_new_info_json(app_info):
    new_app_info={}
    new_app_info['source'] = app_info['source']
    new_app_info['download_time'] = app_info['download_time']
    if 'new' in app_info:
        new_app_info['new'] = 'True'
    return new_app_info


#文件附属信息
def writeApkInfoFile(lock, target_folder, app_info,model='a'):
    with lock:
        with open(target_folder+"cell-"+app_info['MD5'][:2]+"/"+app_info['MD5']+".json", model) as apkInfoFile:
            line = json.dumps(app_info)+"\n"
            apkInfoFile.write(line)

#记录
def writeRecord(lock, target_folder, app_info, model = 'a'):
    with lock:
        with open(target_folder+app_info['download_time'][0:10]+"-record.json", model) as recordFile:
            line = json.dumps(app_info)+"\n"
            recordFile.write(line)

#写log
def write_log(lock, logger, message, level = 'WARN'):
    with lock:
        if logger is None:
            print level, " : ", message
            return
        if level == 'INFO':
            logger.info(message)
        elif level == 'WARN':
            logger.warn(message)
        elif level == 'ERROR':
            logger.error(message)
        elif level == 'DEBUG':
            logger.debug(message)
        elif level == 'CRITICAL':
            logger.critical(message)
        else:
            logger.warn(message)

def write_log_info(lock, logger, message):
    write_log(lock, logger, message, 'INFO')
def write_log_warn(lock, logger, message):
    write_log(lock, logger, message, 'WARN')
def write_log_error(lock, logger, message):
    write_log(lock, logger, message, 'ERROR')
def write_log_debug(lock, logger, message):
    write_log(lock, logger, message, 'DEBUG')
def write_log_critical(lock, logger, message):
    write_log(lock, logger, message, 'CRITICAL')

#browser.get
def browser_get_url(browser,url):
    try:
        browser.get(url)
    except selenium_exception.TimeoutException as e:
        pass

#获取browser的current_url
def get_current_url(browser):
    a = None
    try:
        a = browser.current_url
    except Exception as e:
        pass
    return a


#统一日期格式(将'年','月'等替换为'-'后去除所有非数字和'-'字符,即统一为XXXX-XX-XX格式)
def unify_date(date_str):
    date_str = date_str.strip()
    date_str = date_str.replace("年","-")
    date_str = date_str.replace("月","-")
    date_str = date_str.replace(".","-")
    date_str = date_str.replace("/","-")
    if not '-' in date_str:
        return None
    date_str = filter(lambda ch:ch in '0123456789-',date_str)
    return date_str

#统一下载次数
def unify_download_count(download_count_str):
    download_count_str = download_count_str.strip()
    download_count_str = filter(lambda ch:ch in '.0123456789-十百千万亿',download_count_str)
    t=0
    a = download_count_str.split("-")
    for s in a:
        if "千万" in s:
            t=t+float(s.split("千万")[0])*10000000
        elif "百万" in s:
            t=t+float(s.split("百万")[0])*1000000
        elif "十万" in s:
            t=t+float(s.split("百万")[0])*100000
        elif "万" in s:
            t=t+float(s.split("万")[0])*10000
        elif "千" in s:
            t=t+float(s.split("千")[0])*1000
        elif "百" in s:
            t=t+float(s.split("百")[0])*100
        elif "亿" in s:
            t=t+float(s.split("亿")[0])*100000000
        else:
            t=t+float(s)
    return str(int(t/len(a)))

#处理href属性中的url
def href2url(source,href,current_url):
    if href is None:
        return None
    if href == "":
        return None
    if current_url is None:
        return None
    if href[0:4] != "http":
        if href[0] == "/":
            href = "http://"+source+href
        elif href[0] == '.':
            if (current_url is None) or (current_url == ""):
                return None
            cu = current_url
            cus = cu.split('/')[0:-2]
            href = href[3:]
            cus.extend(href.split('/'))
            s='/'.join(cus)
            href=s
        else:
            if (current_url is None) or (current_url == ""):
                return None
            cu = current_url
            cus = cu.split('/')
            cus[-1] = href
            s='/'.join(cus)
            href = s
    return href

def random_sleep():
    time.sleep(random.randint(1, 3))
