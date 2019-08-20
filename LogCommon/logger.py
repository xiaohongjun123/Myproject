import logging
import time
import os
class mylog(object):
    def __init__(self,logger_name):
        self.logger=logging.getLogger(logger_name)
        self.logger.setLevel(logging.INFO)

        rq=time.strftime('%Y-%m-%d',time.localtime(time.time()))
        all_log_path=os.path.dirname(os.path.abspath(__file__))
        error_log_path=os.path.dirname(os.path.abspath(__file__))
        all_log_name=os.path.join(all_log_path,rq+'.log')
        error_log_name=os.path.join(error_log_path,rq+'error.log')

        fh=logging.FileHandler(all_log_name)
        fh.setLevel(logging.DEBUG)
        eh=logging.FileHandler(error_log_name)
        eh.setLevel(logging.ERROR)
        ch=logging.StreamHandler()
        ch.setLevel(logging.INFO)

        all_log_formatter=logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        error_log_formatter=logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(module)s  - %(lineno)s - %(message)s')

        fh.setFormatter(all_log_formatter)
        ch.setFormatter(all_log_formatter)
        eh.setFormatter(error_log_formatter)
        self.logger.addHandler(fh)
        self.logger.addHandler(eh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger
if __name__=='__main__':
    log=mylog('test').getlog()
    log.info("测试消息")
    log.error('测试错误消息')