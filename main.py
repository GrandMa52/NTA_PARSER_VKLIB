import json

import vk
import pandas as pd
from tqdm import tqdm


def post_parser():
    result = []
    session = vk.Session(access_token='390afbf1390afbf1390afbf1153973c4383390a390afbf158326a7fc9e2a40fff702203')
    vk_api = vk.API(session, v='5.131', lang='ru')
    post_cnt = vk_api.wall.get(domain='nta_ds_ai', count=1)['count']
    for ofs in tqdm(range(0, post_cnt, 100)):
        result.extend(vk_api.wall.get(domain='nta_ds_ai', count=100, offset=ofs)['items'])
    return result


if __name__ == '__main__':
    posts = post_parser()
    df_newpost = pd.DataFrame(columns=['post_id', 'post_link', 'post_title', 'post_view',
                                       'post_source', 'post_likes', 'post_reposts'])
    for post in tqdm(posts):
        if json.dumps(post).find('newtechaudit.ru/'):
            if 'attachments' in post and 'views' in post:  # and (post['attachments'][0].get('link')):
                df_newpost = df_newpost.append({'post_id': post['id'],
                                                'post_link': post['attachments'][0]['link']['url'],
                                                'post_title': post['attachments'][0]['link']['title'],
                                                # 'post_source': post['attachments'][0]['link']['caption'],
                                                'post_view': post['views']['count'],
                                                'post_likes': post['likes']['count'],
                                                'post_reposts': post['reposts']['count']
                                                }, ignore_index=True)
    # df_newpost.to_excel('posts.xlsx', index=False)
    df_newpost.to_csv('posts.txt', sep='|', encoding='utf-8', index=False)
