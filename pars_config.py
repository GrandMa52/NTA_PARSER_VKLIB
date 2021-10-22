import logging


class Config:
    """
    конфигураия API парсера
    """
    # noinspection SpellCheckingInspection
    access_token = '390afbf1390afbf1390afbf1153973c4383390a390afbf158326a7fc9e2a40fff702203'
    ver = '5.131'
    lang = 'ru'
    domain = 'nta_ds_ai'  # текстовый ID группы в ВК


class Logger:
    """
    Конфигурация логирования
    """
    # noinspection SpellCheckingInspection,PyArgumentList
    # for row 22-23 (typo,encoding)
    logging.basicConfig(filename='pars_log.txt',
                        encoding='utf-8',
                        filemode='a',
                        format='%(asctime)s|%(process)d|%(levelname)s|%(message)s',
                        level=logging.INFO)
    log = logging.getLogger('pars_log')
