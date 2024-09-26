# encoding=utf-8
import base64

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


def encrypt(text: str, key: str) -> str:
    iv = "1g3qqdh4jvbskb9x"
    cipher = AES.new(key=key.encode(), mode=AES.MODE_CBC, iv=iv.encode())
    padded_text = pad(text.encode(), AES.block_size)
    result = cipher.encrypt(padded_text)
    return base64.b64encode(result).decode('utf-8')
