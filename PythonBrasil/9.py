# 9) Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
# C = (5 * (F-32) / 9).
temp = float(input('Temperatura em Fahrenheit: '))
print ('Temperatura em Celsius: %.2f' %(5/9 * (temp-32)))