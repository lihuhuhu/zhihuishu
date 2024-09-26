import re

import requests

from config.config import PROXY

params = {
    'key': 'AIzaSyA7O3v41q3HV73ffFGGMmS1nT0m5stIjys',
}


def resolve_question(question: str):
    json_data = {
        'contents': [
            {
                'parts': [
                    {
                        'text': '以一个学生的视角回答这个问题 ' + question,
                    },
                ],
            },
        ],

    }

    response = requests.post(
        'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent',
        params=params,
        json=json_data,
        proxies=PROXY
    )
    return re.sub(r'[*#_\[\]\(\)\{\}<>]', '', response.json()['candidates'][0]['content']['parts'][0]['text'].strip())

if __name__ == '__main__':
    print(resolve_question('你好'))