import re
import hashlib


SENSITIVE_WORDS = {
    "fuck": 0,
    "bitch": 0,
    "习近平": 0,
    "婊": 0
}


"""
函数说明:    检查用户名是否合规
           检查规则:只能包含数字、字母、下划线，长度为3-16个字符
           检查合规返回True，不合规返回False
"""
def check_user_name(name):
    if len(name) > 16:  # 规定用户名不超过16个字符
        return False

    re_pattern = re.compile(r"\w{3,}")  # 规定用户名至少为3个字符
    obj = re.match(re_pattern, name)

    if obj is None:
        return False
    return True


"""
函数说明:     检查字符串中是否包含敏感词汇
返回值说明:   不包含敏感词汇返回True，包含返回False
"""
def has_no_sensitive_word(text):
    global SENSITIVE_WORDS
    for each in SENSITIVE_WORDS.keys():
        if each in text.lower():
            return False
    return True


"""
函数说明:     对用户输入进行哈希加密，哈希函数为sha256
参数说明:     raw_str:需要进行哈希的原文
返回值说明:   sha256结果密文（字符串形式）
"""
def hash_sha256(raw_str):
    hash_func = hashlib.sha256()
    hash_func.update(raw_str.encode("utf-8"))
    return hash_func.hexdigest()


"""
函数说明:     检查用户输入的密码是否合规
            密码设置规则:长度为10-20,必须含有数字、字母以及以下特殊字符:% ! ? # @
参数说明:     pass:需要进行检测的密码字符串
返回值说明:   合规返回True,否则返回False
"""
def check_password(passwd):
    if len(passwd) > 20:  # 必须进行长度限制,正则表达式不能实现长度限制，它只能做到匹配前20项
        return False

    re_pattern = re.compile(r"(?=.*\d)(?=.*[A-Za-z])(?=.*[%!?#@]).{10,}")
    obj = re.match(re_pattern, passwd)

    if obj is None:
        return False
    return True


"""
函数说明:     检查用户输入的电子邮箱地址是否合规
参数说明:     email:需要进行检测的邮箱地址
返回值说明:   合规返回True,否则返回False
"""
def check_email(email):
    re_pattern = re.compile(r"^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$")
    obj = re.match(re_pattern, email)
    if obj is None:
        return False
    return True
