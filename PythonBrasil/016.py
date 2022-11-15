# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

a=float(input("Insira a Altura da parede em metros: "))
l=float(input("Insira a largura da parede em metros: "))
area = a*l
cobertura_tinta = 3
capacidade_lata = 18
preco_lata = 80.00

litros = area / cobertura_tinta
lata_int = int(litros/capacidade_lata)
if (litros%capacidade_lata !=0):
    lata_int +=1
valor = lata_int * preco_lata

print('A área total correponde a',area, 'metros quadrados')
print('São necessarios {} litros de tinta para pintar {} metros² de area'.format(litros, area))
print('São necessarios {} latas de tinta para pintar {} metros² de area'.format(lata_int, area))
print('São necessarios R${} reais para pintar os {} metros² de area'.format(valor, area))
