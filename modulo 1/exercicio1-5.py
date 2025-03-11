def num(n):
    if n==0:
        return "0"
    if n==1:
        return "1"
    return num(n//2)+str(n%2)
print(num(13))
print(num(25))
print(num(14))
print(num(5))
print(num(6))