a=int(input("輸入比數"))
b=["金","銀","銅","優"]
c=[]
for i in range(a):
    c.append(input("輸入"))
    print("%s牌得到%s面"%(b[i],c[i]))