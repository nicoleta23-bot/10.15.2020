a=int(input("dati primul numar: "))
b=int(input("dati al doilea numar: "))
if (a%2==0) and (b%2==0):
    if (a>b):
        print(a)
    else: print(b)
if (a%2==0) and (b%2!=0):
    print(a)
if (a%2!=0) and (b%2==0):
    print(b)
if (a%2!=0) and (b%2!=0):
    print("nu exista numar par")