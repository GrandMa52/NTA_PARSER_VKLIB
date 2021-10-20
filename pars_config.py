import logging


class Config:
    """
    конфигураия API парсера
    """
    access_token = '390afbf1390afbf1390afbf1153973c4383390a390afbf158326a7fc9e2a40fff702203'
    ver = '5.131'
    lang = 'ru'
    domain = 'nta_ds_ai'  # текстовый ID группы в ВК


class Logger:
    """
    Конфигурация логирования
    """
    logging.basicConfig(filename='pars_log.txt',
                        filemode='w',
                        format='%(asctime)s|%(process)d|%(levelname)s|%(message)s',
                        level=logging.INFO)
    log = logging.getLogger('pars_log')
