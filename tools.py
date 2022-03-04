import re


SENSITIVE_WORDS = {
    "fuck": 0,
    "bitch": 0,
    "习近平": 0
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


"""text = '习近平'
print(check_user_name(text))
print(has_no_sensitive_word(text))"""
