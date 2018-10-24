# -*- coding: utf-8 -*-

#ARQUIVO COM TODAS AS OBRAS DO CORPUS OBRAS
CORPUS = 'corpoOBRAS'
#OBRA ESPECÍFICA QUE O USUÁRIO DESEJA EXTRAIR
OBRA = "Aos vinte anos"
#CODIFICAÇÃO DO CORPUS ORIGINAL
CODE = "latin-1"
#CODIFICAÇÃO DA OBRA EXTRAÍDA
CODEFINAL = "latin-1"
###########################################################################

import os

def extrai_obra(corpus, obra):
    livros = list()
    novoarquivo = list()
    corpus = corpus.split('<obra id=')
    for i in corpus:
        livros.append(i.split('</obra>')[0])
    
    for x in livros:
        if '<tituloobra id="' + obra in x:
            novoarquivo = '<obra id=' + x + '</obra>' #'"<$START>"' + '\n' + '<obra_id=' + x + '</obra>'
	
    return novoarquivo


def main():
    arq = open(CORPUS, 'r', encoding=CODE)
    arq = arq.read()
    obra_livro = extrai_obra(arq, OBRA)
    if obra_livro != []:
        if not os.path.exists('obras'):
            os.makedirs('obras')
        arq2 = open('obras/' + OBRA + '.txt', 'w', encoding=CODEFINAL)
        arq2.write(obra_livro)
        arq2.close()
        print ('Obra "' + OBRA + '" extraída com sucesso!')
    else:
        print('Obra "' + OBRA + '" não encontrada.')
    

main()
