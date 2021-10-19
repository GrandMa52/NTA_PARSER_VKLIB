import json
import vk
import pandas as pd
from tqdm import tqdm


# Загрузка постов
# Входные данные: none
# Возвращает: none
def post_parser():
    result = []
    session = vk.Session(access_token='390afbf1390afbf1390afbf1153973c4383390a390afbf158326a7fc9e2a40fff702203')
    vk_api = vk.API(session, v='5.131', lang='ru')
    post_cnt = vk_api.wall.get(domain='nta_ds_ai', count=1)['count']
    for ofs in tqdm(range(0, post_cnt, 100)):
        result.extend(vk_api.wall.get(domain='nta_ds_ai', count=100, offset=ofs)['items'])
    return result


# Функция расчета уникальных просмотров/лайков/репостов
# Входные данные: df: dataframe, type_param: str
# Возвращает: df: dataframe
def calc_unique(df, type_param):
    df['unique_'+type_param] = df['post_'+type_param] - df['post_'+type_param+'_old']
    return df


if __name__ == '__main__':
    posts = post_parser()

    # заполняем dataframe новыми постами
    df_newPosts = pd.DataFrame(columns=['post_id', 'post_link', 'post_title', 'post_views',
                                        'post_likes', 'post_reposts', 'unique_views', 'unique_likes',
                                        'unique_reposts'])
    for post in tqdm(posts):
        if json.dumps(post).find('newtechaudit.ru/'):
            if 'attachments' in post and 'views' in post and (post['attachments'][0].get('link')):
                df_newPosts = df_newPosts.append({'post_id': post['id'],
                                                  'post_link': post['attachments'][0]['link']['url'],
                                                  'post_title': post['attachments'][0]['link']['title'],
                                                  'post_views': post['views']['count'],
                                                  'post_likes': post['likes']['count'],
                                                  'post_reposts': post['reposts']['count'],
                                                  'unique_views': 0,
                                                  'unique_likes': 0,
                                                  'unique_reposts': 0
                                                  }, ignore_index=True)

    # подсчитываем кол-во уникальных просмотров/лайков/репостов
    df_posts = pd.read_csv('posts.txt', sep='|', encoding='utf-8')
    df_newPosts = df_newPosts. \
        merge(df_posts[['post_id', 'post_views', 'post_likes', 'post_reposts']],
              how='left',
              on=['post_id'],
              suffixes=['', '_old'])
    df_newPosts = calc_unique(df_newPosts, 'views')
    df_newPosts = calc_unique(df_newPosts, 'likes')
    df_newPosts = calc_unique(df_newPosts, 'reposts')

    df_newPosts.iloc[:, 0:9].to_csv('posts.txt', sep='|', encoding='utf-8', index=False)
    print('Данные загружены')
