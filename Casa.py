class Casa:
    def __init__(self, cor = None, quartos = None, banheiros = None, tamanho= None):
        self.cor = cor
        self.quartos = quartos
        self.banheiros = banheiros
        self.tamanho = tamanho

    def descrever(self):
        self.cor = input("Cor da casa: ")
        self.quartos = int(input("Número de quartos: "))
        self.banheiros = int(input("Número de banheiros: "))
        self.tamanho = float(input("Tamanho da casa (em m²): "))

        return f"Casa de cor {self.cor}, com {self.quartos} quartos, {self.banheiros} banheiros e tamanho de {self.tamanho} metros quadrados."  

cs = Casa()
print(cs.descrever())  


class Pessoa:
    def __init__(self,nome = None):
        self.nome = nome
        self.nome = input("Nome da pessoa: ")

    def falar(self, mensagem = None):    
        self.mensagem = input("Diga o que você quer falar: ")
        #return f"{self.nome} diz: {self.mensagem}"
    
    def comer(self, comida = None):
        self.comida = input("O que você quer comer?")
        #return f"{self.nome} está comendo {self.comida}"
    
    def dormir(self, horas = None):
        self.horas = input("Quantas horas você quer dormir?")
        #return f"{self.nome} vai dormir por {self.horas}"
    
    def desc(self):
        return f"{self.nome} diz {self.mensagem}, está comendo {self.comida} e vai dormir por {self.horas} horas."
    
p = Pessoa()
p.falar()
p.comer()
p.dormir()
print(p.desc())
