#! /usr/bin/env python3

import sys
import fileinput
import re

text = ""
for line in fileinput.input():
    text += line


# 1. Separar pontuação das palavras
# 2. Marcar capitulos 
# 3. Separar parágrafos de linhas pequenas
# 4. Juntar linhas da mesma frase
# 5. Uma frase por linha

regex_cap = r".*(CAP[IÍ]TULO \w+).* -$"

text = re.sub(regex_cap, r"\n# \1", text)

# regex_nl = r"([a-z0-9,;-])\n\n([a-z0-9])"
# text = re.sub(regex_nl, "\1\n\2", text)

poemas = []

def guarda_poema(poema):
    poemas.append(poema[1])
    return f">>{len(poemas)}<<"

regex_poema = r"<poemas>.*?</poema>"
text = re.sub(regex_poema, guarda_poema, text, flags=re.S)

print(text)
