a=int(input("輸入比數"))
b={}
for i in range(a):
    c=input("輸入英文")
    b[c]=input("輸入中文")
d=input("")
d1=b.get(d)
if d1==None:
    print("未有此單字")
else:
    print("%s中文是%s"%(d,d1))