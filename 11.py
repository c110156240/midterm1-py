a=input("請輸入日期").split(" ")
if int(a[0])==1:
    if int(a[1])>=21:
        print("aqusurius")
    else:
        print("Capricorn")
if int(a[0])==2:
    if int(a[1])>=19:
        print("pisces")
    else:
        print("aqusurius")
if int(a[0])==3:
    if int(a[1])>=21:
        print("aries")
    else:
        print("pisces")
if int(a[0])==4:
    if int(a[1])>=21:
        print("tauris")
    else:
        print("aries")
if int(a[0])==5:
    if int(a[1])>=22:
        print("gemini")
    else:
        print("tauris")
if int(a[0])==6:
    if int(a[1])>=22:
        print("cancer")
    else:
        print("gemini")
if int(a[0])==7:
    if int(a[1])>=23:
        print("leo")
    else:
        print("cancer")
if int(a[0])==8:
    if int(a[1])>=24:
        print("virgo")
    else:
        print("leo")
if int(a[0])==9:
    if int(a[1])>24:
        print("libra")
    else:
        print("virgo")
if int(a[0])==10:
    if int(a[1])>24:
        print("scorpio")
    else:
        print("libra")
if int(a[0])==11:
    if int(a[1])>23:
        print("sagittarius")
    else:
        print("scorpio")
if int(a[0])==12:
    if int(a[1])>22:
        print("Capricorn")
    else:
        print('sagittarius')