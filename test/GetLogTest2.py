import logging
import logging.config
# logging.basicConfig(filename='t.log',level=logging.DEBUG)
logging.config.fileConfig('logFile.conf')
logger = logging.getLogger('GetLogTest2')

class A():
    def __init__(self):
        # logging.config.fileConfig('logFile.conf')
        self.logger = logging.getLogger('A logger')
    def logFunc(self):
        self.logger.debug('debug message')
        self.logger.info('info message ')
        self.logger.warn('warn message')
        self.logger.error('error messages')
        self.logger.critical('critical message')
        return 'its A class'

class B():
    def __init__(self):
        self.logger = logging.getLogger('B logger')
    def logFuncTest(self):
        self.logger.debug('debug message logFuncTest')
        self.logger.info('info message logFuncTest')
        self.logger.warn('warn message logFuncTest')
        self.logger.error('error messages logFuncTest')
        self.logger.critical('critical message logFuncTest')
        return 'its B class'
def logFunction():
    logger.debug('debug message logFuncTest')
    logger.info('info message logFuncTest')
    logger.warn('warn message logFuncTest')
    logger.error('error messages logFuncTest')
    logger.critical('critical message logFuncTest')
    return 'logFunction is return'

a = A()
print a.logFunc()
# b = B()
# print b.logFuncTest()
# print(logFunction())