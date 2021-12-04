import re

def leave_DNA(matchobj): #strr - слово, имеет в себе буквы д, н, к
    strr = matchobj.group(0)
    m = re.match(r'(.*)д(.*)н(.*)к(.*)', strr[:-1])
    res = ' '*len(m.groups()[0])+'д'+' '*len(m.groups()[1])+'н'+' '*len(m.groups()[2])+'к'+' '*len(m.groups()[3]) + strr[-1]
    return  res

if __name__=='__main__':
    with open('example.txt', 'r',  encoding='UTF8') as file:
        text = file.read()
    print(text)
    print(re.sub(r'([ёа-я]*д[ёа-я]*н[ёа-я]*к[ёа-я]*[ .,!?$])', leave_DNA, text))
