# 0->а, 32->я
#ord('a')==1072, ord('я')=1103, ё нет в ord
strr = ''
while True:
    a = input()
    if a == 'End':
        break
    a = int(a)
    if a == -1:
        strr += ' '
    elif 0<=a<=5:
        strr += chr(1072+a)
    elif a == 6:
        strr += 'ё'
    elif 7<=a<=32:
        strr += chr(1072+a-1)
print(strr)