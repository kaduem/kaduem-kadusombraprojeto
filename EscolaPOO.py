class Escola:
    def __init__(self, nome= None, endereco= None, telefone= None, salas= None, tamanho= None):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.salas = salas
        self.tamanho = tamanho

    def descrever(self):
        self.nome = input("Nome da escola: ")
        self.endereco = input("Endereço da escola: ")
        self.telefone = input("Telefone da escola: ")
        self.salas = int(input("Número de salas: "))
        self.tamanho = float(input("Tamanho da escola (em m²): "))

        return f"Escola {self.nome}, localizada em {self.endereco}, telefone {self.telefone}, com {self.salas} salas e tamanho de {self.tamanho} metros quadrados."

es = Escola()
print(es.descrever())        