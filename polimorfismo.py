class Pato:
    def quack(self):
        print("o pato faz Quack!")

class Pessoa:
    def quack(self):
        print("a pessoa imita um pato: Quack!")

    def comer(self):
        print("a pessoa está comendo")

def fazer_quack(obj):
    obj.quack()

p = Pato()
h = Pessoa()

class Gravacao:
    def quack(self):
        print("Som gravado: Quack quack!")

class Robo:
    def quack(self):
        print("Robo: Q-U-A-C-K!")

objetos = [Pato(), Pessoa(), Gravacao(), Robo()]

for obj in objetos:
    obj.quack()