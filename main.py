import vk


def post_parser():
    session = vk.Session(access_token='390afbf1390afbf1390afbf1153973c4383390a390afbf158326a7fc9e2a40fff702203')
    vk_api = vk.API(session, v='5.131', lang='ru')
    result = vk_api.wall.get(domain='nta_ds_ai', count=100)
    posts = result['items']
    return posts


if __name__ == '__main__':
    print(len(post_parser()))
