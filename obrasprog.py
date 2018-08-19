import re
import os

def leark():
    OBRAS = "OBRAS_completo_VISL.vislcg3"
    arq = open(OBRAS,'r', encoding="latin-1")
    arq = arq.read()
    arq = arq.split('\n')
    return arq


lk = list()
for i in leark():
    if 'tituloobra_id' in i:
        lk.append(i)
    
lk2 = list()
for i in lk:
    i = i.split('"')
    lk2.append(i[1])
    
lk2 = '\n'.join(lk2)
    
print(lk2)
    
arq = open('titulos_obras.txt','w', encoding="utf-8")
arq.write(lk2)
arq.close()