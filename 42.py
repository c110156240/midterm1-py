a=int(input("a"))
b=int(input("b"))
c=int(input("c"))
x=(-b+(b*b-4*a*c)**0.5)/2*a
x1=(-b-(b*b-4*a*c)**0.5)/2*a
if b*b-4*a*c<0:
    print(0)
elif x==x1:
    print("{:.0f}".format(x))
else:
    print("{:.0f}".format(x))
    print("{:.0f}".format(x1))


