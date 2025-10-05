def num(num1):
    if num1>0:
        return num1 + num(num1-1)
    else:
        return 0
