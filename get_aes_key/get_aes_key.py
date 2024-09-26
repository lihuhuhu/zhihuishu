import requests

from config.config import aes_headers
from util.create_uid import uid


def aes_key_cypher() -> str:
    params = {
        "uid": uid()}
    url = 'https://appcomm-user.zhihuishu.com/app-commserv-user/c/hasV2'
    response = requests.get(url, params=params, headers=aes_headers)
    return response.json()['rt'].get('sl')


if __name__ == '__main__':
    print(aes_key_cypher())
