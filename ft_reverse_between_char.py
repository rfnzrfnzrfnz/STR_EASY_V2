def ft_len(stsr):
    l = 0
    for i in stsr:
        l += 1
    return l


def ft_find_char(char, sstr):
    count = 0
    x = 0
    r = 0
    if char in sstr:
        for i in range(ft_len(sstr)):
            if str[i] == char:
                x = i
                break
        for i in sstr:
            if i == char:
                count += 1
        if count == 1:
            return x
        else:
            for i in range(ft_len(sstr)):
                if sstr[i] == char:
                    r = i
            return x, r
    else:
        return False


def ft_reverse_str(sstr):
    a = ''
    for i in range(-1, -ft_len(sstr) - 1, -1):
        a += sstr[i]
    return a


def ft_reverse_between_char(char, stsr):
    b = 0
    for i in stsr:
        if i == char:
            b += 1
    if b == 0:
        return -2
    elif b == 1:
        return -1
    a, c = ft_find_char(char, stsr)
    return ft_reverse_str(stsr[a + 1:c])
