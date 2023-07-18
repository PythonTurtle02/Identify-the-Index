# www.youtube.com/@pythonturtle

text1 = "dhayajune2345678"
text2 = "dhayajune2945678"

zip_texts = zip(text1, text2)
# print(list(zip_texts))

enum_texts = enumerate(zip_texts)
# print(list(enum_texts))

for i, (a, b) in enum_texts:
    if a != b:
        print(f'index {i}')
