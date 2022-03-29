a=int(input("請輸入正整數"))
b=[]
i=2
for i in range(2,a):
   j=2
   for j in range(2,i):
      if(i%j==0):
         break
   else:
      b.append(i)
if b==[]:
    print("no prime found")
b.sort
c=b.pop()
print(c)