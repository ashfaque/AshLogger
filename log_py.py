# ? https://realpython.com/python-logging/

import logging

logging.basicConfig(
    filename='logs/log_file_name.log'
    , filemode='a'
    # , format='[%(asctime)s.%(msecs)d] %(levelname)s [%(name)s:%(lineno)s] [%(module)s.%(funcName)s] [%(process)d.%(thread)d] %(message)s'
    , format='[%(asctime)s.%(msecs)d] %(levelname)s [%(name)s:%(lineno)s] [%(module)s.%(funcName)s] ===> %(message)s'
    , datefmt='%Y-%m-%d %H:%M:%S'
    , level=logging.DEBUG
)

logger = logging.getLogger(__name__)

logger.info(f'{1} info log')
logger.debug('%s debug log', 2)
logger.warning('{0} warning log'.format(3))
logger.error('4 error log')
