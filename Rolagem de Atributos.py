import random

dados = [0] * 7
def rolagem_atributos():
  for i in range(7):
    dado = random.randint(1, 20)
    dados[i] = dado
  dados.sort(reverse = True)
  print(dados)
  print('Menor valor: %d\n'%(dados.pop()), 'Números finais: ', dados)
  
  #print(dados,'\nMenor valor: %d\n'%(dados.pop()), 'Números finais: ', dados)

rolagem_atributos()
