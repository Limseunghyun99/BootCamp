def input_func():
    raw_input = input()
    try:
        raw_input = int(raw_input)
    except ValueError:
        print("입력은 정수여야 합니다.")
        return None
    
    raw_input = str(raw_input)
    
    c = 0
    if raw_input[0] == '-':
        c = len(raw_input[1:])
    else:
        c = len(raw_input)
    
    if c > 20:
        print("정수 N의 자릿수는 최대 20자리입니다.")
        return None

    return raw_input

def function(raw_string):
    ret = ""
    neg_flag = False
    if raw_string[0] == '-':
        neg_flag = True
        raw_string = raw_string[1:]

    for i, e in enumerate(raw_string[::-1], start=1):
        ret += e + ("," if i % 3 == 0 else "")
    ret = ret[::-1]

    if ret[0] == ',':
        ret = ret[1:]
    
    if neg_flag:
        ret = '-' + ret

    print(ret)


if __name__ == '__main__':
    c = 0
    while c < 3:
        a = input_func()
        if a == None:
            c += 1
            continue
        else:
            function(a)
            exit(0)
    print("연속으로 3번 이상 잘못된 입력입니다.")