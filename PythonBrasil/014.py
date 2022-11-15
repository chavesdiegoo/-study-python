#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de SP (50 quilos)
# deve pagar uma multa de R$ 4,00 por quilo excedente.
#
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
# Imprima os dados do programa com as mensagens adequadas.


peso_peixe =float(input("Insira os quilos pescado: "))

limite = 50
excesso = peso_peixe - 50
multa_kg= 4
multa = excesso * multa_kg
if peso_peixe > limite:
    print('Peso acima do limite em {}Kg. Multa no valor de R$ {:.2f}'.format(peso_peixe - limite, multa))
else:
    print('Peso dentro do limite de', limite,'Kg. Não Taxado!')

