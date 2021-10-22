import pars_config
from pars_config import Logger
from tqdm import tqdm
import vk


class Parsers(pars_config.Config):

    @property
    def wall_parser(self):
        """
        Выгрузка постов со стены ВК
        :return: list
        """
        print('Загрузка постов')
        Logger.log.info('Запущена загрузка постов')

        result = []
        # noinspection PyBroadException
        # for row 27
        try:
            session = vk.Session(access_token=self.access_token)
            vk_api = vk.API(session, v=self.ver, lang=self.lang)
            post_cnt = vk_api.wall.get(domain=self.domain, count=1)['count']
            for ofs in tqdm(range(0, post_cnt, 100)):
                result.extend(vk_api.wall.get(domain=self.domain, count=100, offset=ofs)['items'])
        except Exception:
            Logger.log.error('Произошла ошибка, парсер остановлен: ', exc_info=True)
            exit()

        print('Загрузка постов завершена')
        Logger.log.info('Завершена загрузка постов')
        return result
