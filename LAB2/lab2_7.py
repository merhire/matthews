text = "А роза упала на лапу Азора"

text = text.replace(" ", "")

text = text.lower()

reversed = ""
for ch in text:
    reversed += ch
if text == reversed:
    print("Это палиндром")
else:
    print("Это не палиндром")
