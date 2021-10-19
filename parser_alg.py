import parsers_module as prs_m
import data_proc as d_proc


class Parsing:
    print('Парсер запущен')
    pars_list = prs_m.Parsers().wall_parser()
    d_proc.Data_proc(pars_list).wall_proc()
    print('Парсер завершил работу')
