def solution(plain):
    answer = 0
    p_len = len(plain)
    is_pal = is_p(plain, p_len)
    check = ""
    if is_pal:
        answer = p_len
    else:
        for i in range(p_len-1, 0, -1):
            check += plain[p_len-i-1]
            num = p_len + len(check)
            answer = num
            if is_p(plain+check, num):
                break
    return answer

def  is_p(str, len):
    for i in range(len // 2):
        if str[i] == str[::-1][i]:
            continue
        else:
            return False
    return True

print(solution('abcde'))