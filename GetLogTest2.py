import logging
import logging.config
logging.basicConfig(filename='t.log',level=logging.DEBUG)
logging.config.fileConfig('logFile.conf')
logger = logging.getLogger('simpleExample')

logger.debug('debug message')
logger.info('info message ')
logger.warn('warn message')
logger.error('error messages')
logger.critical('critical message')

