#A entrada consiste no número de dados, seguido da letra "d" e logo após o tipo de dado e o valor a ser somado
# EXEMPLOS DE ENTRADAS: 1d20, 5d10, 2d6+5, 1d20+7
import random
numero = input('Digite o número de dados e o tipo: (EX: 4d12 ou 1d20+8) ')
numero = numero.replace('d','+')
lnumero = numero.split('+')
soma = 0
cont = 1
for i in range(int(lnumero[0])):
  x = random.randint(1,int(lnumero[1]))
  print('Dado %d -> %d'%(cont,x))
  cont += 1
  soma += x
if len(lnumero) > 2:
  soma = soma+int(lnumero[2])
print('Valor Final: %d'%soma)
