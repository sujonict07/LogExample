import logging

print __name__
logging.basicConfig(filename='test.log',level=logging.INFO)
logger = logging.getLogger('GetLogTest')
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s -- %(name)s- %(levelname)s-- %(message)s')

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

ch.setFormatter(formatter)
logging.FileHandler

logger.addHandler(ch)
logger.debug('logger debug test')
logger.info('this is info')
logger.warn('warn message ')
logger.error('error messages')
logger.critical('critical messages')