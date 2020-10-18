n1=int(input("dati numarul elevului 1: "))
n2=int(input("dati numarul elevului 2: "))
n3=int(input("dati numarul elevului 3: "))
p1=int(input("dati punctajul elevului n1: "))
p2=int(input("dati punctajul elevului n2: "))
p3=int(input("dati punctajul elevului n3: "))
if (p1>p2) and (p1>p3):
    print(n1)
if (p2>p1) and (p2>p3):
    print(n2)
if (p3>p1) and (p3>p2):
    print(n3)
if (p1==p3) and (p1>p2) and (p3>p2):
    print(n1, n3)
if (p1==p2) and (p1>p3) and (p2>p3):
    print(n1, n2)
if (p2==p3) and (p2>p1) and (p3>p1):
    print(n2, n3)
if (p1==p2) and (p1==p3) and (p2==p3):
    print("punctajul egal la toti 3 elevi")