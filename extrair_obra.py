import os

def extrai_obra(obras, obra):
    livros = list()
    novoarquivo = list()
    obras = obras.split('<obra_id=')
    for i in obras:
        livros.append(i.split('</obra>')[0])
    
    for x in livros:
        if '<tituloobra_id="' + obra in x:
            novoarquivo = '"<$START>"' + '\n' + '<obra_id=' + x + '</obra>'
	
    return novoarquivo


def main(obra):
    arq = 'OBRAS_completo_VISL.vislcg3'
    arq = open(arq, 'r', encoding="latin-1")
    arq = arq.read()
    obra_livro = extrai_obra(arq, obra)
    if obra_livro != []:
        if not os.path.exists('obras'):
            os.makedirs('obras')
        arq2 = open('obras/' + obra + '.vislcg3', 'w', encoding="utf-8")
        arq2.write(obra_livro)
        arq2.close()
        print ('Obra "' + obra + '" extraída com sucesso!')
    else:
        print('Obra "' + obra + '" não encontrada.')
    

obra = "Aos_vinte_anos"
main(obra)