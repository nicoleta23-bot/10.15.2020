a=int(input("dati primul nr: "))
b=int(input("dati al doilea nr: "))
c=int(input("dati al treilea nr: "))
if (a>=0) and (b>=0) and (c>=0):
    if (b>c):
        print(b)
    else: print(c)
if (a<0) or (b<0) or (c<0):
    print(a+b)