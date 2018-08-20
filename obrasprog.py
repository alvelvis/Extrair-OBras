#ARQUIVO COM TODAS AS OBRAS DO CORPUS OBRAS
CORPUS = "OBRAS_completo_VISL.vislcg3"
#CODIFICAÇÃO DO CORPUS ORIGINAL
CODE = "latin-1"
#CODIFICAÇÃO DA OBRA EXTRAÍDA
CODEFINAL = "latin-1"
#####################################################

import re
import os

def leark():
    arq = open(CORPUS,'r', encoding=CODE)
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
    
arq = open('titulos_obras.txt','w', encoding=CODEFINAL)
arq.write(lk2)
arq.close()