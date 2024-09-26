# request
port = '7897'
PROXY = {'https': f'127.0.0.1:{port}', 'http': f'127.0.0.1:{port}'}

# cookies = {
#     'exitRecod_X9DyBNvB': 'dfasdfasdf',
#     'Hm_lvt_0a1b7151d8c580761c3aef32a3d501c6': ',',
#     'CASTGC': '',
#     'CASLOGC': '',
#     'jt-cas': '.',
#     'SESSION': 'w',
#     'acw_tc': 'ac110',
#     'SERVERID': 'f',
# }

aes_headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Origin': 'https://qah5.zhihuishu.com',
    'Pragma': 'no-cache',
    'Referer': 'https://qah5.zhihuishu.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'Origin': 'https://qah5.zhihuishu.com',
    'Pragma': 'no-cache',
    'Referer': 'https://qah5.zhihuishu.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

# js中固定的值
rsa_public_key = """-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCgfZmpLpPEpEFRKBe+ZjWJUjPe
+7qg7pGqcfN3j2egJ8H2mrKwaEqZEnPnpi2O3hN8HRyaFozDOp8gwZiYfiIZjWy0
Jr/FNAiiKYh5bq0GsEn+ieMmRyJg/+i1rqizhvCXvFdrdGhFTw5EBwTpsGdwe1ut
dlrvIJUAFWj9Yh4qbQIDAQAB
-----END PUBLIC KEY-----"""

# encrypt
COURSE_KEY = "7q9oko0vqb3la20r"
