a=input("輸入").split(" ")
b=0
for i in range(len(a)):
    if a[i]=="A":
        b=b+1
    elif a[i]=="J":
        b=b+11
    elif a[i]=="Q":
        b=b+12
    elif a[i]=="K":
        b=b+13
    else:
        b=b+int(a[i])
print(b)