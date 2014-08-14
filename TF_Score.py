#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  TF_Score.py
#  
#  Copyright 2014 Leandro <Leandro@leandrowar>
#  
#Calculo dos scores de frequencia

documentos = { 
 'StarWars4' : "No caminho de ampliar o imperio intergalactico, as hostes do Lado Negro da Forca comandadas pelo sinistro Darth Vader e pelo Imperador Palpatine sequestram a princesa Leia Organa e destroem o seu planeta. No entanto, dois robos, R2D2 e C3PO , conseguem escapar. No planeta Tatooine, Owen Lars, o tio de Luke Skywalker, compra os dois robos e com eles encontra uma mensagem da princesa Leia para o jedi Obi-Wan Kenobi sobre os planos da construcao da Estrela da Morte, uma gigantesca estacao espacial com capacidade para destruir um planeta.",
 'StarWars5' : "Tres anos depois da destruicao da Estrela da Morte, a Alianca Rebelde arranjou uma base no planeta gelado Hoth. Mas as forcas do Imperio os descobre, e sob o comando de Darth Vader os ataca com os AT-AT. Os sobreviventes se espalham. Luke Skywalker, seguindo a orientacao do espirito de Obi-Wan Kenobi, vai para o planeta pantanoso Dagobah, encontrar o outrora mais poderoso Jedi, Yoda, e com ele terminar seu treinamento. Ja Han Solo, a princesa Leia Organa e Chewbacca encaminham-se para o planeta Bespin onde eles foram recebidos por um velho amigo de Han, um esperto jogador chamado Lando Calrissian. Emboscados pelo Imperio assim que chegaram, Han e seus amigos sao aprisionados por Darth Vader.",
 'StarWars6' : "Luke Skywalker voltou ao seu planeta natal, Tatooine, na tentativa de salvar seu amigo Han Solo das garras de Jabba, o Hutt. Luke ainda nao sabe que o Imperio Galactico iniciou secretamente a construcao de uma nova estacao espacial belica, mais poderosa que a primeira e temida Estrela da Morte. Quando estiver pronta, esta arma definitiva certamente significara o fim do pequeno grupo de rebeldes que luta para devolver a liberdade a galaxia..."
}
terms = {
 'StarWars4' : [ i.lower() for i in documentos['StarWars4'].split() ],
 'StarWars5' : [ i.lower() for i in documentos['StarWars5'].split() ],
 'StarWars6' : [ i.lower() for i in documentos['StarWars6'].split() ]
 }


def tf(termo, doc, normalize=True):
    doc = doc.lower().split()
    if normalize:
        return doc.count(termo.lower()) / float(len(doc))
    else:
        return doc.count(termo.lower()) / 1.0

i = 0
for each in documentos:
	print documentos.keys()[i] + ' TF - ' + str(tf('Luke',documentos[each]))
	i = i + 1

print 




def main():
	
	return 0

if __name__ == '__main__':
	main()

