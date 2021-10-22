import parsers_module as prs_m
import data_proc as d_proc
from pars_config import Logger as Logger


class Parsing:
    Logger.log.info('Запуск парсера')
    print('Парсер запущен')

    # noinspection PyBroadException
    # for row 15
    try:
        pars_list = prs_m.Parsers().wall_parser
        d_proc.Data_proc(pars_list).wall_proc()
    except Exception:
        Logger.log.error('Произошла ошибка, парсер остановлен: ', exc_info=True)
        exit()

    Logger.log.info('Завершение работы парсера')
    print('Парсер завершил работу')
