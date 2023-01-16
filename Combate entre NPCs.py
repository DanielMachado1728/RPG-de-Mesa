import random

class Personagem():
  def __init__(self, nome, ataque, forca, defesa, arma, dano_arma, vida):
    self.nome = nome
    self.ataque = ataque
    self.forca = forca
    self.defesa = defesa
    self.arma = arma
    self.dano_arma = dano_arma
    self.vida = vida

  def atacar(self):
    rolagem_dados = random.randint(2,12)
    ataque = rolagem_dados + self.ataque 
    print('%s ataque: %d + %d = %d'%(self.nome, rolagem_dados, self.ataque, ataque))
    return ataque

  def defender(self):
    rolagem_dados = random.randint(2,12)
    defesa = rolagem_dados + self.defesa
    print('%s defesa: %d + %d = %d'%(self.nome, rolagem_dados, self.defesa, defesa))
    return defesa

  def dar_dano(self):
    rolagem_dados = random.randint(2,12)
    dano = rolagem_dados + self.forca  + self.dano_arma
    print('Dano dado por %s: %d + %d + %d = %d'%(self.nome, rolagem_dados, self.forca, self.dano_arma, dano))
    return dano

  def mostrar_personagem(self):
    print('\nNome: %s\nAtaque: %d\nForça: %d\nDefesa: %d\nArma: %s\nDano da arma: %d\nVida: %d'%(self.nome, self.ataque, self.forca, self.defesa, self.arma, self.dano_arma, self.vida))

  def iniciativa(self):
    rolagem_dados = random.randint(2,12)
    print('Iniciativa do(a) %s: %d'%(self.nome, rolagem_dados))
    return rolagem_dados


#FUNÇÃO DE CRIAÇÃO DOS PERSONAGENS
def construção(i):
  nome = input('Digite o nome do personagem %d: '%(i+1))
  ataque = int(input('Digite o valor de ataque do(a) %s: '%nome))
  forca = int(input('Digite a força do(a) %s: '%nome))
  defesa = int(input('Digite a defesa do(a) %s: '%nome))
  arma = input('Digite o nome da arma do(a) %s: '%nome)
  dano_arma = int(input('Digite o dano de sua arma: '))
  vida = int(input('Digite a vida do(a) %s: '%nome))

  personagem = Personagem(nome, ataque,forca, defesa, arma, dano_arma, vida)
  #personagem.mostrar_personagem()
  personagens.append(personagem)
  return personagens


#INÍCIO DO CÓDIGO (CHAMADA ÀS FUNÇÕES E CRIAÇÃO DAS INSTÂNCIAS DA CLASSE "Personagem")
print()
personagens = []
for i in range(2):
  construção(i)
  print()

iniciativa1 = personagens[0].iniciativa()
iniciativa2 = personagens[1].iniciativa()

if iniciativa1 > iniciativa2:
  primeiro = personagens[0]
  segundo = personagens[1]
else:
  primeiro = personagens[1]
  segundo = personagens[0]

rodada = 0
# jeito de pegar atributos --> a = personagens[0].vida
while primeiro.vida > 0 or segundo.vida > 0:
  rodada += 1
  print('\nRodada %d\n'%rodada)
  if primeiro.atacar() > segundo.defender():
    segundo.vida -= primeiro.dar_dano()
    print('Vida atual do(a) %s: %d'%(segundo.nome, segundo.vida))
    if segundo.vida <= 0:
      break
  else:
    print('%s desviou do ataque.'%segundo.nome)
  if segundo.atacar() > primeiro.defender():
    primeiro.vida -= segundo.dar_dano()
    print('Vida atual do(a) %s: %d'%(primeiro.nome, primeiro.vida))
    if primeiro.vida <= 0:
      break
  else:
    print('%s desviou do ataque.'%primeiro.nome)
