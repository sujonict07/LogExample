import logging

logger = logging.getLogger('logExample')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s -- %(name)s- %(levelname)s-- %(message)s')

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

ch.setFormatter(formatter)


logger.addHandler(ch)
logger.debug('logger debug test')
logger.info('this is info')
logger.warn('warn message ')
logger.error('error messages')
logger.critical('critical messages')