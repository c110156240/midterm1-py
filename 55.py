a=["飢餓遊戲3","解憂雜貨店","怪獸與他們的產地","哈利波特6","我的阿富汗筆友","祈念之樹","樓下的房客","小王子"]
b=["房思琪的初戀樂園","等一個人的咖啡","鬼滅之刀14","神農嘗百草","麥田補手","老人與海","傲慢與偏見","與神同行"]
c=input("請輸入要找的書名")
if c in a:
    print("在A書架的第%s本"%(a.index(c)+1))
elif c in b:
    print("在B書架的第%s本"%(b.index(c)+1))    
else:
    print("查無此書籍")








