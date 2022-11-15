# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados
# 11% para o Imposto de Renda,
# 8% para o INSS
# e 5% para o sindicato,
# faça um programa que nos dê:
# salário bruto. quanto pagou ao INSS. quanto pagou ao sindicato. o salário líquido.

salario=float(input("Insira o Salario do Colaborador R$: "))
desc_inss = (salario * 8/100)
desc_irpf = (salario * 11/100)
desc_sind = (salario * 5/100)

#horas=float(input("Insira a quantidade de horas trabalhadas: "))
print('O Salário Bruto no referido mes é de R${:.2f} Tendo os seguintes descontos:\nFoi descontato referente ao IRPF R$ {:.2f}'.format(salario, (salario*11/100)))
print('Foi descontato referente ao INSS :R${:.2f}'.format((salario*8/100)))
print('Foi descontato referente ao Sindicato :R${:.2f}'.format((salario*5/100)))
print('O salário liquido do contribuinte é de :R$ {:.2f}'.format((salario - desc_sind - desc_inss - desc_irpf)))
