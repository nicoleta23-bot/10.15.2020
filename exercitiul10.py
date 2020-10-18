n1=int(input("Introduceti numarul de gaini : "))
n2=int(input("Introduceti numarul de boabe : "))
nbg=n2//n1
nbc=n2-(n1*nbg)
if (nbg>nbc) :
    print("Gaina primeste mai mult cu : ",nbg-nbc,"boabe")
if (nbc>nbg) :
    print("Curcanul primeste mai mult cu : ",nbc-nbg,"boabe")    
else :
    print("primesc acelasi numar de boabe")