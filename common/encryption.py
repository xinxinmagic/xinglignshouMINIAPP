# ----------------------- #
#    author:zhangxin      #
#                         #
#      time:20200923      #
#                         #
# ----------------------- #
import ctypes
import hashlib


def int_overflow(val):
    # 因python左移没有溢出的概念，int左移如果溢出会自动变为long型，所以手动写一个左移溢出
    maxint = 2147483647
    if not -maxint - 1 <= val <= maxint:
        val = (val + (maxint + 1)) % (2 * (maxint + 1)) - maxint - 1
    return val


def unsigned_right_shift(n, i):
    # 数字小于0，则转为32位无符号uint
    if n < 0:
        n = ctypes.c_uint32(n).value
    # 正常位移位数是为正数，但是为了兼容js之类的，负数就右移变成左移好了
    if i < 0:
        return -int_overflow(n << abs(i))
    # print(n)
    return int_overflow(n >> i)


def base36_encode(number):
    """
    10进制转化为36进制
    :param number:
    :return:
    """
    num_str = '0123456789abcdefghijklmnopqrstuvwxyz'
    if number == 0:
        return '0'
    base36 = []
    while number != 0:
        number, i = divmod(number, 36)  # 返回 number// 36 , number%36
        base36.append(num_str[i])
    print(''.join(reversed(base36)))
    return ''.join(reversed(base36))


def generate_psw(psw):
    """
    :return: 返回加密后的密码
    """
    m = hashlib.md5()
    b = ("rCt52pF2cnnKNB3Hkp" + psw).encode(encoding='utf-8')
    m.update(b)
    return m.hexdigest()


def id_encry(id):
    """
    主键id加密
    :param id:
    :return:
    """
    version = 1
    sb = ""
    sb1 = sb + str(version)
    id_e = base36_encode(id * 2 + 56)
    url = sb1 + str(id_e)
    return url


def urltoid(url):
    """
    解密id
    :param url:
    :return:
    """
    version =1
    url_1= url[version:len(url)]
    id = (int(url_1,36)-56)/2
    return int(id)

def sign_encry(default_header, custom_param):
    """
    :return: 生成sv，并返回拼接后的完整headers
    """
    v = {}
    v.update(default_header)
    v.update(custom_param)
    keys = list(v.keys())
    keys.sort()
    print("加密前 key%d", str(keys))
    # create the string to be signed
    valuesStr = ''
    for key in keys:
        if v[key]:
            valuesStr += str(v[key])
    if len(valuesStr) < 8:
        valuesStr += '0123456789012345'
    print("加密前value %d", valuesStr)
    # 排序序列
    s1 = [0 * i for i in range(0, 8)]
    for i in range(0, len(valuesStr) // 8 - 1):
        for j in range(0, 8):
            if (i + 1) * 8 + j < len(valuesStr):
                if i == 0:
                    s1[j] = ord(valuesStr[i * 8 + j])
                s1[j] ^= ord(valuesStr[(i + 1) * 8 + j])
    # encode the bytes to string
    encodeStr = ''
    # 排序密码表
    HEX_TAB_WEB = "s~0!e@5#c$8%r^6&"
    sum = 0
    for i in range(0, 8):
        # 获取密码指针
        r1 = unsigned_right_shift(s1[i], 3) & 0xF
        r2 = s1[i] & 0xF
        tempS = HEX_TAB_WEB[r1] + HEX_TAB_WEB[r2]
        encodeStr += tempS
        sum += ord(HEX_TAB_WEB[r1])
    # 末尾两个干扰码
    encodeStr += HEX_TAB_WEB[sum % 16]
    encodeStr += HEX_TAB_WEB[sum % 13]
    default_header['s'] = encodeStr
    return default_header
