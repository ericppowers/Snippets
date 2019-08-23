"""
This code is meant to display using an .ini file for configuration settings to make things easier for end-users.

The configuration settings can be found under config.ini, and the log file created is log.txt

import logging

def logs(settings='config.ini'):
    with open(settings, 'r') as f:
        config = []
        read = f.read()
        for item in read.splitlines():
            config.append(item.split('='))
    logging.basicConfig(filename=config[1][1],
                        level=config[3][1],
                        format=config[0][1],
                        datefmt=config[2][1])
    logger = logging.getLogger(__name__)
    return logger

log = logs()
"""

import logging


def logs(settings='config.ini'):
    with open(settings, 'r') as f:
        config = []
        read = f.read()
        for item in read.splitlines():
            config.append(item.split(' : '))
    logging.basicConfig(filename=config[1][1],
                        level=config[3][1],
                        format=config[0][1],
                        datefmt=config[2][1])
    logger = logging.getLogger(__name__)
    return logger


def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    return x / y


def expo(x, y):
    """Exponent Function"""
    return x ** y


def modulo(x, y):
    """Modulo Function"""
    return x % y


def fl_div(x, y):
    """Floor Division Function"""
    return x // y


def nums(num_1, num_2):
    log = logs()
    try:
        add_result = add(num_1, num_2)
        log.debug(f'Add: {num_1} + {num_2} = {add_result}')

        sub_result = subtract(num_1, num_2)
        log.debug(f'Sub: {num_1} - {num_2} = {sub_result}')

        mul_result = multiply(num_1, num_2)
        log.debug(f'Mul: {num_1} * {num_2} = {mul_result}')

        div_result = divide(num_1, num_2)
        log.debug(f'Div: {num_1} / {num_2} = {div_result}')

        expo_result = expo(num_1, num_2)
        log.debug(f'Exp: {num_1} / {num_2} = {expo_result}')

        mod_result = modulo(num_1, num_2)
        log.debug(f'Mod: {num_1} / {num_2} = {mod_result}')

        fl_div_result = fl_div(num_1, num_2)
        log.debug(f'Floor: {num_1} / {num_2} = {fl_div_result}')
    except Exception as err:
        log.exception(f'An error has occurred.\n')


for i in range(-10, 11):
    for m in range(-10, 11):
        nums(i, m)
