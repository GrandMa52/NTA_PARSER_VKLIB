import json
import pandas as pd
from tqdm import tqdm
from pars_config import Logger


class Data_proc:

    def __init__(self, wall_list):
        self.wall_list = wall_list

    @staticmethod
    def calc_unique(df, type_param):
        """
        Подсчет уникальных показателей поста
        :param df: dataframe
        :param type_param: str
        :return: dataframe
        """
        df['unique_' + type_param] = df['post_' + type_param] - df['post_' + type_param + '_old']
        return df

    def wall_proc(self):
        """
        Обработка выгруженных постов
        :return: None
        """
        Logger.log.info('Запущена обработка постов')
        print('Обновляем данные о постах')

        # noinspection PyBroadException
        # for row 64
        try:
            df_new_posts = pd.DataFrame(columns=['post_id', 'post_link', 'post_title', 'post_views',
                                                 'post_likes', 'post_reposts', 'unique_views', 'unique_likes',
                                                 'unique_reposts'])
            for post in tqdm(self.wall_list):
                if json.dumps(post).find('newtechaudit.ru/'):
                    if 'attachments' in post and 'views' in post and (post['attachments'][0].get('link')):
                        df_new_posts = df_new_posts.append({'post_id': post['id'],
                                                            'post_link': post['attachments'][0]['link']['url'],
                                                            'post_title': post['attachments'][0]['link']['title'],
                                                            'post_views': post['views']['count'],
                                                            'post_likes': post['likes']['count'],
                                                            'post_reposts': post['reposts']['count'],
                                                            'unique_views': 0,
                                                            'unique_likes': 0,
                                                            'unique_reposts': 0
                                                            }, ignore_index=True)

            df_posts = pd.read_csv('posts.txt', sep='|', encoding='utf-8')
            # noinspection PyTypeChecker
            # for row 58
            df_new_posts = df_new_posts. \
                merge(df_posts[['post_id', 'post_views', 'post_likes', 'post_reposts']],
                      how='left',
                      on=['post_id'],
                      suffixes=['', '_old'])
            df_new_posts = self.calc_unique(df_new_posts, 'views')
            df_new_posts = self.calc_unique(df_new_posts, 'likes')
            df_new_posts = self.calc_unique(df_new_posts, 'reposts')

            df_new_posts.iloc[:, 0:9].to_csv('posts.txt', sep='|', encoding='utf-8', index=False)
        except Exception:
            Logger.log.error('Произошла ошибка, парсер остановлен: ', exc_info=True)
            exit()

        print('Данные по постам обновлены')
        Logger.log.info('Завершена обработка постов')
