xa=int(input("dati nr de bile albe mici: "))
xr=int(input("dati nr de bile rosii mici: "))
xv=int(input("dati nr de bile verzi mici: "))
ya=int(input("dati nr de bile albe mari: "))
yr=int(input("dati nr de bile rosii mari: "))
yv=int(input("dati nr de bile verzi mari: "))
xt = xa+xr+xv
yt = ya+yr+yv
print("total=", xt+yt, "bile")
if (xt>yt):
    print(xt,"bile mici" ", "  "bile mici sunt mai multe")
else: print(yt,"bile mari" ", " "bile mari sunt mai multe")
if (xt==yt):
    print("numar egal de bile mici si mari")
if ((xa+ya)>(xr+yr)) and ((xa+ya)>(xv+yv)):
    print("albe: ",xa+ya, "bile" )
if ((xr+yr)>(xa+ya)) and ((xr+yr)>(xv+yv)):
    print("rosii: ", xr+yr, "bile")
if ((xv+yv)>(xa+ya)) and ((xv+yv)>(xr+yr)):
    print("verzi: ", xv+yv, "bile")
if ((xa+ya)==(xr+yr)):
    if ((xa+ya)>(xv+yv) and (xr+yr))>(xv+yv):
        print("albe: ", xa+ya, "bile",  "rosii: ", xr+yr, "bile")   
if ((xa+ya)==(xv+yv)):
    if ((xa+ya)>(xr+yr)) and ((xv+yv)>(xr+yr)):
        print("albe: ", xa+ya, "bile",  "verzi: ", xv+yv, "bile")
if ((xr+yr)==(xv+yv)):
    if ((xr+yr)>(xa+ya)) and ((xv+yv)>(xa+ya)): 
        print("rosii: ", xr+yr, "bile",  "verzi: ", xv+yv, "bile")
if ((xa+ya)==(xr+yr)) and ((xa+ya)==(xv+yv)) and ((xr+yr)==(xv+yv)):
    print("albe: ", xa+ya, "bile",  "rosii: ", xr+yr, "bile", "verzi: ", xv+yv, "bile", "numar de bile egale")

