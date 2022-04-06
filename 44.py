a=int(input("幾班"))
b=[]
for i in range(a):
    b.append(int(input("輸入班級人數")))
b.sort()
print(b[-1])