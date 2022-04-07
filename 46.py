a1=input("輸入1、2(key、item)")
if a1=="1":
    r=[]
    b=["金","銀","銅","優"]
    t={}
    a=int(input("輸入比數"))
    for i in range(a):
        r.append(input("輸入"))
        t[b[i]]=r[i]
        print("%s牌得到%s面"%(b[i],t.get(b[i])))

else:
    a=int(input("輸入比數"))
    b=["金","銀","銅","優"]
    c=[]
    for i in range(a):
        c.append(input("輸入"))
        print("%s牌得到%s面"%(b[i],c[i]))
