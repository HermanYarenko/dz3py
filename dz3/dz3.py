eng = {1:'AEIOULNSTRaeioulnstr', 2: 'DGdg', 3:'BCMPbcmp', 4:'FHVWYfhvwy', 5: 'Kk', 8: 'JXjx', 10: 'QZqz'}
rus = {1: 'АВЕИНОРСТавеинорст', 2: 'ДКЛМПУдклмпу', 3: 'БГЁЬЯбгёья', 4: 'ЙЫqs', 5: 'ЖЗХЦЧжзхцч', 8: 'ШЭЮшэю', 10: 'ФЩЪфщъ'}
res = 0
word = str (input('Введите слово: '))

alph = ["а","б","в","г","д","е","ё","ж","з","и","й","к","л","м",
        "н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я",
        "А","Б","В","Г","Д","Е","Ё","Ж","З","И","Й","К","Л","М","Н","О","П","Р","С",
        "Т","У","Ф","Х","Ц","Ч","Ш","Щ","Ъ","Ы","Ь","Э","Ю","Я"]
if word[0] in alph:
    for i in word:
        for k,v in rus.items():
            if i in v:
                res += k
    print(f'стоимость введенного слова равна {res} баллов')
else:
    for i in word:
        for k,v in eng.items():
            if i in v:
                res += k
    print(f'стоимость введенного слова равна {res} баллов')