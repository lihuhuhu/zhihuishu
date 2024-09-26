# encoding=utf-8
import base64
import json
import rsa

from config.config import rsa_public_key


def base64_to_hex(cypher: str) -> str:
    return base64.b64decode(cypher).hex()


def decrypt_with_public_key(encrypted_hex, public_key) -> bytes:
    """
    使用 RSA 公钥解密以十六进制格式提供的消息
    """
    try:
        # 将十六进制字符串转换为整数
        encrypted_int = int(encrypted_hex, 16)

        # 执行公钥的模幂运算：m = c^e mod n
        decrypted_int = pow(encrypted_int, public_key.e, public_key.n)

        # 计算字节长度并转换为字节
        byte_length = (decrypted_int.bit_length() + 7) // 8
        decrypted_bytes = decrypted_int.to_bytes(byte_length, 'big')

        return decrypted_bytes
    except ValueError as e:
        raise ValueError("加密数据格式不正确或无法转换为整数。") from e


def decrypt(crypt_base64: str) -> str:
    cypher_hex = base64_to_hex(crypt_base64)
    public_key = rsa.PublicKey.load_pkcs1_openssl_pem(rsa_public_key.encode('utf-8'))
    result_bytes = decrypt_with_public_key(cypher_hex, public_key)
    str_dict = ''
    for i in result_bytes[74:]:
        if i < 128:
            str_dict += chr(i)
    result = json.loads(str_dict)
    return result.get('cKey')