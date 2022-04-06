a=int(input("幾個地方"))
b=[]
for i in range(a):
    b.append(int(input("幾公里")))
    if b[i] %9==0 or b[i]%11==0:
        print("第%d個點%d"%(i+1,b[i]))
