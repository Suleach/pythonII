alpha_eng = "qwertyuiop[]asdfghjkl;'zxcvbnm,. "
alpha_rus = "йцукенгшщзхъфывапролджэячсмитьбю "
text = "руддщ"
encode = ""
for i in range(len(text)):
    for j in range(len(alpha_rus)):
        if text[i]==alpha_rus[j]:
            encode = encode + alpha_eng[j]
print(encode)