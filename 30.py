ans="1234"
o=0
while o!=1:
    a=input("輸入")
    b=0
    c=0
    if a=="0000":
        o=1
    for i in range(4):
        for j in range(4):
            if ans[i] == a[j]:
                if a[i]==ans[i]:
                    b=b+1
                else:
                    c=c+1
    print("%dA%dB"%(b,c))


