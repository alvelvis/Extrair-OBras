#ARQUIVO COM TODAS AS OBRAS DO CORPUS OBRAS
CORPUS = 'OBRAS_completo_VISL.vislcg3'
#OBRA ESPECÍFICA QUE O USUÁRIO QUER EXTRAIR
OBRA = "A_Mortalha_de_Alzira"
#CODIFICAÇÃO DO CORPUS ORIGINAL
CODE = "latin-1"
###########################################################################

import os

def extrai_obra(corpus, obra):
    livros = list()
    novoarquivo = list()
    corpus = corpus.split('<obra_id=')
    for i in corpus:
        livros.append(i.split('</obra>')[0])
    
    for x in livros:
        if '<tituloobra_id="' + obra in x:
            novoarquivo = '"<$START>"' + '\n' + '<obra_id=' + x + '</obra>'
	
    return novoarquivo


def main():
    arq = open(CORPUS, 'r', encoding=CODE)
    arq = arq.read()
    obra_livro = extrai_obra(arq, OBRA)
    if obra_livro != []:
        if not os.path.exists('obras'):
            os.makedirs('obras')
        arq2 = open('obras/' + OBRA + '.vislcg3', 'w', encoding=CODE)
        arq2.write(obra_livro)
        arq2.close()
        print ('Obra "' + OBRA + '" extraída com sucesso!')
    else:
        print('Obra "' + OBRA + '" não encontrada.')
    

main()