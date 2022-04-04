a=input("輸入一字元")
b=len(a)/2
c=0
for i in range(int(b)):
    if a[i]==a[-i-1]:
        c=1
    else:
        c=0
if c==1:
    print("yes")
else:
    print("no")