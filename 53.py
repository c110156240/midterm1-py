a=int(input("輸入"))
b={}
for i in range(a):
    c=input("name")
    d=input("e-mail")
    b[c]=d
e=input("請輸入要查詢的名子")
print("%s電子信箱為%s"%(e,b[e]))