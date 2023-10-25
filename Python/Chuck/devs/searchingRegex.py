import re

hand = open('/Users/leonardo/Desktop/Leo/Cursos/Cursos/Python/Chuck/Apuntes/Files/mbox-short.txt')
for line in hand:
    line=line.rstrip()
    if re.search('From:', line):
        print(line)

for line in hand:
    line=line.rstrip()
    if re.search('^From:', line):
        print(line)