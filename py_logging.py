# ? https://realpython.com/python-logging/
# ? https://note.nkmk.me/en/python-script-file-path/

import logging
import os

logging.basicConfig(
    # ! '../logs/log_file_name.log' will make `logs` one dir back.
    # filename=os.path.join(os.path.dirname(__file__), 'logs/log_file_name.log')    # Py 3.9 onwards always returns absolute path.
    filename=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs/log_file_name.log')    # Py 3.8 or earlier returns relative or absolute path if its provided while running the .py file.
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
