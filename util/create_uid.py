import base64

import rsa

from config.config import rsa_public_key


def uid() -> str:
    """
    :return: base64
    """
    source_text = '{"module":10}'.encode('utf-8')
    public_key = rsa.PublicKey.load_pkcs1_openssl_pem(rsa_public_key.encode())
    cypher = rsa.encrypt(source_text, public_key)
    return base64.b64encode(cypher).decode()


if __name__ == '__main__':
    print(uid())
