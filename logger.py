import logging


def get_configured_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler('logger.log')
    file_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger


module_logger = get_configured_logger('test.logger')


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        module_logger.exception('Tried to divide by zero')
    else:
        return result


num_1 = 10
num_2 = 0
div_result = divide(num_1, num_2)
module_logger.info('Div: {} / {} = {}'.format(num_1, num_2, div_result))

