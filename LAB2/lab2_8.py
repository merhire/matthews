words = ["кот", "машина", "программирование", "дом"]
word = ""
max_l = 0
for i in words:
        if len(i) > max_l:
                max_l = len(i)
                word = i
print("bolshaya - ", max_l, " у ", word)