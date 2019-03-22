def try_div(x):
    if x:
        return 5/x
    else:
        raise ZeroDivisionError

print(try_div(0))