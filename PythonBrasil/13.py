# Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu
# peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7 (h = altura)
# Peça o peso da pessoa e informe se ela está dentro, acima ou abaixo do peso.

sexo =int(input("Escolha: 1 - Masc / 2 - Fem "))
alt =float(input("Informe a altura: "))
peso=float(input("Peso: "))

pesoi = (72.7*alt) - 58 if sexo == 1 else (62.1*alt) - 44.7
if peso < pesoi:
	print('Abaixo do peso ideal!')
elif peso == pesoi:
	print('Dentro do peso ideal!')
else:
	print('Acima do peso ideal!')
print ('Peso: %.2f / Peso ideal: %.2f' %(peso, pesoi))
