n=int(input("輸入"))
a=[]
while n!=1:
    if n%2==0:
        n=n/2
        a.append("{:.0f}".format(n))
    else:
        n=3*n+1
        a.append("{:.0f}".format(n))
print(a)