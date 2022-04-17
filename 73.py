a1=input("1")
a=a1.split(":")
b=int(input("2"))
d=(int(a[0])*60+int(a[1]))*60+int(a[2])
    
c=b%60
c1=int(b/60)%60
c2=int(int(b/60)/60)
print("%s=%d"%(a1,d))
print("%d=%d:%d:%d"%(b,c2,c1,c))












