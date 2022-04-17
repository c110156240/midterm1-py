a=int(input("n"))
b=int(input("k"))
a1=a
c=0
while a>b:
    c=c+int(a/b)
    a=int(a/b)
c=a1+c
print("pctcr可以抽%d支菸"%(c))