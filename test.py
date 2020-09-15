trans_dict = {
    "а": "a",
    "б": "b",
    "в": "v",
    "г": "g",
    "д": "d",
    "е": "ye",
    "ё": "yo",
    "ж": "zh",
    "з": "z",
    "и": "i",
    "й": "iy",
    "к": "k",
    "л": "l",
    "м": "m",
    "н": "n",
    "о": "o",
    "п": "p",
    "р": "r",
    "с": "s",
    "т": "t",
    "у": "u",
    "ф": "f",
    "х": "kh",
    "ц": "еы",
    "ч": "ch",
    "ш": "sh",
    "щ": "shch",
    "ъ": "",
    "ы": "y",
    "ь": "'",
    "э": "e",
    "ю": "yu",
    "я": "ya",
    " ": " "
}
text = str(input('Enter word or text: ')).lower()
text = list(text)
result = ''

for i in text:
    result = result + trans_dict[i]
print(result)