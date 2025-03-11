def num(n):
    if n == 1:
        return n
    else:
       return  n+num(n-1)
print(num(5))
print(num(13))