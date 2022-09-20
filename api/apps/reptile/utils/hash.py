from hashlib import md5


def my_md5(msg):
    """
    md5加密算法
    :param msg: 需要加密的字符串
    :return: 返回加密后的字符串
    """
    h1 = md5()
    h1.update(msg.encode("utf-8"))
    return h1.hexdigest().lower()
