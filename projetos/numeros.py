n = int(input())

while(n > 0):
    a = input()
    b = input()
    veficador = True

    if len(a) < len(b):
        print("nao")
        break
    
    j = 0
    i = (len(a) - len(b))
    for i in range(len(a) - len(b), len(a)):
        if(a[i] != b[j]):
            veficador = False
        j += 1
    if veficador == True:
        print("encaixa")
    else:
        print("nao")
    n -= 1
