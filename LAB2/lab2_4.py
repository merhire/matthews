num1 = "112233332211"
num2 = "112233332211"

poli = 1  

for i in range(len(num1)):
    if num1[i] != num2[len(num2) - 1 - i]:
        poli = 0
        break

if poli == 1:
    print("они палиндромы")
else:
    print("не палиндромы")
