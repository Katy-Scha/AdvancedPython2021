import re

def cut_currency(strr):
    return re.sub(r'[€\$₽]', '', strr)

if __name__=='__main__':
    text = 'Молоко стоит $2. Один билет в Сан-Франциско и обратно стоит 30000 ₽, а 2 билета — всего 50000₽! €1 = 83₽ (2021 год, 22 ноября).'
    print(text)

    all = re.findall(r'[€\$₽] ?[0-9]+|[0-9]+ ?[€\$₽]', text)
    print(all)   #если нужно найти с единицами валюты

    #print(list(map(cut_currency, all)))   #если нужно найти без единиц валюты