alpha_eng = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
alpha_rus = "йцукенгшщзхъфывапролджэячсмитьбю"

def encode(text):
    encode = ""
    for i in range(len(text)):
        for j in range(len(alpha_eng)):
            if text[i]==alpha_eng[j]:
                encode = encode + alpha_rus[j]
    return encode

def decode(text):
    decode = ""
    for i in range(len(text)):
        for j in range(len(alpha_rus)):
            if text[i]==alpha_rus[j]:
                decode = decode + alpha_eng[j]
    return decode

text = str(input("Enter text: "))
text = text.lower()

if text[0] in alpha_rus:
    right = decode(text)
if text[0] in alpha_eng:
    right = encode(text)
print(right)