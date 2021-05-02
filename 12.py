n = input("輸入一整數序列為：").split(" ")
list1 = []
for i in range(0, len(n)):
    a = 0
    for j in range(0, len(n)):
        if n[i] == n[j]:
            a += 1
    list1.append(a)

if max(list1)>len(n)/2:
    for x in range(0,len(list1)):
        if max(list1)==list1[x]:
            print("過半元素為:"+n[x])
            break
else:
    print("過半元素為:No")
print(list1)
