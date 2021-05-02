bir=input("請輸入月即日為:").split(" ")
ch=int(bir[0])*30+int(bir[1])

print("星座為:",end="")
if 51<=ch<=78:
    print("Aquarius")
if 79<=ch<=110:
    print("Pisces")
if 111<=ch<=150:
    print("Aries")
if 151<=ch<=171:
    print("taurus")
if 172<=ch<=201:
    print("Gemini")
if 202<=ch<=232:
    print("Cancer")
if 233<=ch<=263:
    print("leo")
if 264<=ch<=293:
    print("Virgo")
if 294<=ch<=323:
    print("Libra")
if 324<=ch<=381:
    print("射手")
if ch>=382 and ch<=50:
    print("魔羯")
