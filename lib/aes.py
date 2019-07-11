# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
import binascii

BS = AES.block_size
AES_SECRET_KEY = '990AD535ED164E13990D7507CDDDF8t1'
IV = 'XXXXXXXXXXXXXXXX'
ens = 'PoLKM%X3v#U@nb*NMxz!1O$U^WNvk1L2m84756'

pad = lambda s: s + (BS - len(bytes(s, encoding='utf-8')) % BS) * chr(BS - len(bytes(s, encoding='utf-8')) % BS)
unpad = lambda s: s[0:-ord(s[-1:])]

def getSen(mkey):
    s = ''
    for x in mkey:
        index = hex(ens.index(x))[2:]
        s += index
    return s

# 加密函数
def encrypt(text):
    cryptor = AES.new(AES_SECRET_KEY.encode("utf8"), AES.MODE_CBC, getSen(IV).encode("utf8"))
    ciphertext = cryptor.encrypt(bytes(pad(text), encoding="utf8"))
    return binascii.b2a_hex(ciphertext).decode().upper()

# 解密函数
def decrypt(text):
    cryptor = AES.new(AES_SECRET_KEY.encode("utf8"), AES.MODE_CBC, getSen(IV).encode("utf8"))
    plain_text = cryptor.decrypt(binascii.a2b_hex(text))
    return unpad(plain_text).decode()


if __name__ == '__main__':
    e = encrypt("缩缩缩")
    d = encrypt("ff")
    print(len("缩缩缩"))
    print(e)
    print(d)