def function():
    ret = ""
    for i, e in enumerate((raw_string:=input())[::-1], start=1):
        ret += e + ("," if i % 3 == 0 else "")
    ret = ret[::-1]
    if ret[0] == ',':
        ret = ret[1:]
    print(ret)


if __name__ == '__main__':
    function()