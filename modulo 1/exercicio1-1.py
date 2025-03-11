def intervalo(a,b):
    if a > b:
        print("Intervalo inválido")
        return
    if a==b:    
        print (a,end = ' ')
    else:
        print(a,end = ' ')
        intervalo(a+1,b)
intervalo(1,10) 
intervalo(-5,1)
intervalo(5,-5)
intervalo(17,20)
