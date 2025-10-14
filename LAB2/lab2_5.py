list = [1,2,3,4,5,6,7,8,9,12,15]
new_list = []
for i in range(len(list)):
    if list[i]%3==0:
        new_list.append(list[i])
print(new_list)