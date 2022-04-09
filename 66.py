a=input("請輸入")
b=input("請輸入")
c=""
d=""
e=""
for t in range(len(a)):
    for h in range(t+1,len(a)):
        if a[t]==a[h]:
            break
    else:
        d=d+a[t]
for t1 in range(len(b)):
    for h1 in range(t+1,len(b)):
        if b[t1]==b[h1]:
            break
    else:
        e=e+b[t1]
for i in range(len(d)):
    for j in range(len(e)):
        if d[i]==e[j]:
            c=c+d[i]
            break
print(d)
print(e)
if c=="":
    print("N")
else:
    print(c)








