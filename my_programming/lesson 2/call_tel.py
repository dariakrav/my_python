def call_tell(code, length):
    if code == 343:
        print(length*15)
    elif code == 381:
        print(length*18)
    elif code == 473:
        print(length*13)
    else:
        print(length*11)

call_tell(343, 350)