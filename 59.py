a=int(input("money"))
b=0
while a!=0:
    if a>=100:
        b=b+int(a/100)
        a=a%100
    elif a>=50:
        b=b+int(a/50)
        a=a%50
    elif a>=10:
        b=b+int(a/10)
        a=a%10
    elif a>=5:
        b=b+int(a/5)
        a=a%5
    else:
        b=b+int(a/1)
        a=a%1
print(b)
