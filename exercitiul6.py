n1=int(input("dati prima nota: "))
n2=int(input("dati a doua nota: "))
n3=int(input("dati a treia nota: "))
if (n3>=8):
    print(n1, " " ,n2, " " ,n3)
if (n3<8):
    if (n1>n2):
        print(n1)
    else: print(n2)