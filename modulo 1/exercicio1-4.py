def num(n,div=None):
    if n<2:
        return False
    if div is None:
        div = n - 1
    if div==1:
        return True
    if n % div == 0:
        return False
    return num(n,div-1)
print(num(7))
print(num(10))
print(num(9))
print(num(131))
print(num(25))