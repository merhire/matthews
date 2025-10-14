n = int(input("Enter n: "))
sum = 0
for i in range(n):
    if i%2 == 0:
        sum = sum + i;
print(sum)