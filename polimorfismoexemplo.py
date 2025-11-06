class Atacante:
    def gol(self):
        print("------Funções Jogadores------\no Atacante faz gol!")

class Meia:
    def gol(self):
        print("o Meia arma jogadas para gol")

class Zagueiro:
    def gol(self):
        print("o Zagueiro defende o gol")

class Goleiro:
    def gol(self):
        print("o Goleiro defende o gol")

def fazer_gol(obj):
    obj.gol()

a = Atacante()
m = Meia()
z = Zagueiro()
g = Goleiro()

objetos = [Atacante(), Meia(), Zagueiro(), Goleiro()]
for obj in objetos:
    obj.gol()
#_________________________________________________________________________________________________
print("------Funções Diretorias------")
class Presidente:
    def funcao(self):
        print("o Presidente cuida do gerenciamento geral do clube!")

class Treinadordegoleiro:
    def funcao(self):
        print("o Treinador de Goleiros, treina os goleiros do clube e cuida do mental deles também!")

class AuxiliarTecnico:
    def funcao(self):
        print("o Auxiliar Tecnico auxilia o tecnico à beira do campo")

class PreparadorFísico:
    def funcao(self):
        print("o Preparador Físico cuida do físico e da peformances dos jogadores dentro de campo ")

class Contador:
    def funcao(self):
        print("o Contador cuida do que entra e sai do financeiro do clube")
class Olheiro:
    def funcao(self):
         print("o Olheiro é responsável na contratação de jogadores para o clube e em achar novos talentos para o futuro da equipe")

def diretoria(obj):
    obj.função()

p = Presidente()
t = Treinadordegoleiro()
a = AuxiliarTecnico()
p = PreparadorFísico()
c = Contador()
o = Olheiro()

objetos = [Presidente(), Treinadordegoleiro(), AuxiliarTecnico(), PreparadorFísico(), Contador(), Olheiro()]
for obj in objetos:
    obj.funcao()

