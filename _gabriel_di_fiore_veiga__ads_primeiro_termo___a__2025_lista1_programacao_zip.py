# -*- coding: utf-8 -*-
"""<Gabriel Di Fiore Veiga>_ADS<Primeiro termo>_<A>_2025_lista1_programacao.zip

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Fjs9VZkoy4MGPDzwOKxHv5wgTUKnSDxm

Exercicio 1
"""

M = float(input('O valor em metros : '))
print(f'o valor de {M}m em centimetros é {M*100}cm')

"""Exercicio 2"""

v1 = float(input('quantas horas você trabalha no mês : '))
v2 = float(input('quanto você recebe por hora : '))
print(f'você recebe {v1*v2}reais por mês')

"""Exercicio 3"""

t1 = float(input('me diga a temperatura em graus fahrenheit : '))
tc = 5*(t1-32)/9
print(f'a temperatura em graus celsius é {tc}')

"""Exercicio 4"""

p = float(input('me diga o seu peso em kg : '))
a = float(input('me diga a altura em metros: '))
imc = p/(a**2)
print(f"o seu valor de imc é {imc}")

"""Exercicio 5"""

peso = float(input("Digite o peso dos peixes em quilos: "))

if peso > 30:
    excesso = peso - 30
    multa = excesso * 3
    print(f"O peso dos peixes é {peso} quilos.")
    print(f"Excesso de {excesso} quilos.")
    print(f"Multa a pagar: R$ {multa}")
else:
    print(f"O peso dos peixes é {peso} quilos. Não há excesso. Não há multa.")

"""Exercicio 6"""

vh = float(input("Valor/hora: R$ "))
ht = float(input("Horas/mês: "))


sb = vh * ht


ir = sb * 0.11
inss = sb * 0.08


sl = sb - (ir + inss)

print("\nDetalhamento do Salário:")
print(f"Salário Bruto: R$ {sb}")
print(f"IR (11%): R$ {ir}")
print(f"INSS (8%): R$ {inss}")
print(f"Salário Líquido: R$ {sl}")

"""Exercicio 7"""

m2 = float(input('Me fale o valor da parede em metros quadrados : '))
m3 = m2/3
m4 = m3/18
m5 = m4*80#
print(f'A quantidade de latas necessarias são :{m4}latas')
print(f'O valor das latas serão: {m5}reais')

"""Exercicio 7 Feito para uma loja"""

import math

m2 = float(input('Me fale o valor da parede em metros quadrados: '))
m3 = m2 / 3
m4 = m3 / 18
m4_arredondado = math.ceil(m4)
m5 = m4_arredondado * 80

print(f'A quantidade de latas necessárias são: {m4_arredondado} latas')
print(f'O valor das latas será: {m5} reais')
# teste foda 2.0
#macumba


