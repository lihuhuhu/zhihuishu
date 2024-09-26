# encoding=utf-8
import json
import random
import time
from typing import Generator

import requests

from chatgpt_api.chatgpt_api import resolve_question
from config.config import COURSE_KEY, cookies, headers
from get_aes_key.get_aes_key import aes_key_cypher
from zhiihuishu.crypt.encrypt import encrypt
from zhiihuishu.crypt.decrypt import decrypt
requests = requests.session()


def submit_answer(question_info: dict, reply: str) -> None:
    """
    提交问题答案
    :param question_info:
    :param reply:
    :return:
    """
    text = {"annexs": "[]", "qid": question_info['questionId'], "source": "2", "aContent": reply,
            "courseId": question_info["courseId"], "recruitId": question_info["recruitId"], "saveSource": 1}
    data = {
        'dateFormate': f'{int(time.time() * 1000)}',
        'secretStr': encrypt(json.dumps(text), SUBMIT_KEY)
    }
    response = requests.post(
        'https://creditqa-api.zhihuishu.com/creditqa/gateway/t/v1/web/qa/saveAnswer',
        cookies=cookies,
        headers=headers,
        data=data,
    )
    print(response.text)


def get_course_question(courseId: str, recruitId: str) -> dict:
    """
    获取问题
    :param courseId: 课程id
    :param recruitId: 获取最新问题的id
    :return:最新的问题
    """
    cypher = {"courseId": courseId, "pageIndex": 0, "pageSize": 50, "recruitId": recruitId}
    data = {
        'dateFormate': f'{int(time.time() * 1000)}',
        'secretStr': encrypt(json.dumps(cypher), SUBMIT_KEY)
    }

    response = requests.post(
        'https://creditqa-api.zhihuishu.com/creditqa/gateway/t/v1/web/qa/getRecommendList',
        cookies=cookies,
        headers=headers,
        data=data,
    )
    return response.json()


def handle_question(response_result: dict) -> Generator[dict, dict, None]:
    """
    生成器
    :param response_result:
    :return:
    """
    print(response_result)
    for item in response_result['rt']['questionInfoList']:
        yield item


def handle_course(course_info: dict) -> None:
    """
    遍历每个课程
    :param course_info:
    :return:
    """
    questions = get_course_question(course_info['courseId'], course_info['recruitId'])
    for question in handle_question(questions):
        time.sleep(random.randint(3, 10))
        answer = resolve_question(question['content'])
        submit_answer(question, answer)


def get_course() -> dict:
    url = 'https://onlineservice-api.zhihuishu.com/gateway/t/v1/student/course/share/queryShareCourseInfo'
    cypher = {"status": 1, "pageNo": 1, "pageSize": 5}
    data = {
        'secretStr': encrypt(json.dumps(cypher, separators=(',', ':')), COURSE_KEY),
        'date': f'{int(time.time() * 1000)}',
    }
    return requests.post(url=url, headers=headers, data=data, cookies=cookies).json()


def get_aes_key() -> str:
    cypher = aes_key_cypher()
    assert cypher, "网络问题或者其更换加密方式"
    return decrypt(cypher)


if __name__ == '__main__':
    SUBMIT_KEY = get_aes_key()
    # 获取所有课程
    courses = get_course()
    print(courses)
    for course in courses['result']['courseOpenDtos']:
        handle_course(course)
