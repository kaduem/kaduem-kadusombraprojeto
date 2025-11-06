class Pessoa:
    def __init__(self, nome: str = None, idade: int = None):
        if nome is None:
            nome = input("Nome da pessoa: ")
        if idade is None:
            idade = int(input("Idade da pessoa: "))
        
        self.nome = nome
        self.idade = idade


class Jogador(Pessoa):
    def __init__(self,nome: str = None, idade: int = None, posicao: str = None, numero: int = None):
        if nome is None:
            nome = input("Nome do jogador: ")
        if idade is None:
            idade = int(input("Idade do jogador: "))
        if posicao is None:
            posicao = input("Posição do jogador: ")
        if numero is None:
            numero = int(input("Número do jogador: "))
        super().__init__(nome, idade)
        self.posicao = posicao
        self.numero = numero

class Tecnico(Pessoa):
    def __init__(self, nome: str = None, idade: int = None, experiencia: int = None):
        if nome is None:
            nome = input("Nome do técnico: ")
        if idade is None:
            idade = int(input("Idade do técnico: "))
        if experiencia is None:
            experiencia = int(input("Anos de experiência do técnico: "))
        
        super().__init__(nome, idade)
        self.experiencia = experiencia  

    
class Clube:
    def __init__(self, nome):
        self.nome = nome
        self.jogadores = []
        self.tecnicos = None

    def contratar_jogador(self, jogador):
        self.jogadores.append(jogador)
    def contratar_tecnico(self, tecnico):
        self.tecnicos = tecnico

    def mostrar_elenco(self):
        print(f"Clube: {self.nome}")
        print("Técnico:")
        if self.tecnicos:
            print(f"Nome: {self.tecnicos.nome}, Idade: {self.tecnicos.idade}, Experiência: {self.tecnicos.experiencia} anos")
        else:
            print("Nenhum técnico contratado.")
        print("Jogadores:")
        for jogador in self.jogadores:
            print(f"Nome: {jogador.nome}, Idade: {jogador.idade}, Posição: {jogador.posicao}, Número: {jogador.numero}")

    def mostrar_tecnico(self):
        if self.tecnicos:
            print(f"Técnico do clube {self.nome}:")
            print(f"Nome: {self.tecnicos.nome}, Idade: {self.tecnicos.idade}, Experiência: {self.tecnicos.experiencia} anos")
        else:
            print("Nenhum técnico contratado.")                     

def menu_pricipal():
    clube_nome = input("Digite o nome do clube: ")
    clube = Clube(clube_nome)

    while True:
        print("\nMenu:")
        print("1. Contratar Jogador")
        print("2. Contratar Técnico")
        print("3. Mostrar Elenco")
        print("4. Mostrar Técnico")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            jogador = Jogador()
            clube.contratar_jogador(jogador)
        if escolha == '2':
            tecnico = Tecnico()
            clube.contratar_tecnico(tecnico)
        if escolha == '3':
            clube.mostrar_elenco()
        if escolha == '4':
            clube.mostrar_tecnico()
        if escolha == '5':
            print("Saindo do programa.")
            break

if __name__ == "__main__":
    menu_pricipal()