class Pessoa:
    def __init__(self, nome: str, cpf: str) -> None:
        self.nome = nome
        self.cpf = cpf

    def apresentar(self) -> str:
        return f"Olá, meu nome é {self.nome}, CPF: {self.cpf}."
    
class Aluno(Pessoa):
    def __init__(self, nome= None, cpf= None, matricula= None):
        if nome is None:
            nome = input("Nome do aluno: ")
        if cpf is None:
            cpf = input("CPF do aluno: ")
        if matricula is None:
            matricula = input("Matrícula do aluno: ")

        super().__init__(nome, cpf)
        self.matricula = matricula

    def apresentar(self):
        base = super().apresentar()
        return f"{base} Sou aluno, matrícula {self.matricula} e CPF {self.cpf}."

# class Aluno(Pessoa):
#     def __init__(self, nome: str, cpf: str, matricula: str) -> None:
#         super().__init__(nome, cpf)
#         self.matricula = matricula

#     def apresentar(self) -> str:
#         base = super().apresentar()
#         return f"{base} Sou aluno, matrícula {self.matricula}."
    
class Professor(Aluno):
    def __init__(self, nome = None, matricula= None, disciplina= None, cpf= None) -> None:
        if nome is None:
            nome = input("Nome do professor: ")
        if cpf is None:
            cpf = input("CPF do professor: ")
        if disciplina is None:
            disciplina = input("Disciplina do professor: ")
        if matricula is None:
            matricula = input("Matrícula do professor: ")

        super().__init__(nome,cpf, matricula)
        self.disciplina = disciplina

    def apresentar(self):
        base = super().apresentar()
        return f"{base} Sou professor da disciplina {self.disciplina} com matrícula {self.matricula} e CPF {self.cpf}."

p = Pessoa("João", "111.222.333-44")
a = Aluno()
pr = Professor()
        
print(p.apresentar())
#print(a.apresentar())      
print(pr.apresentar())
# class Professor(Pessoa):
#     def __init__(self, nome: str, cpf: str, disciplina: str) -> None:
#         super().__init__(nome, cpf)
#         self.disciplina = disciplina

#     def apresentar(self) -> str:
#         return f"Professor {self.nome}, CPF: {self.cpf}, é professor de {self.disciplina}."
    

# class BolsaMixin:
#     def calcular_bolsa(self) -> float:
#         return 1200.0


# class AlunoBolsista(BolsaMixin, Aluno):
#     def apresentar(self) -> str:
#         base = super().apresentar()
#         return f"{base} Minha bolsa é de R$ {self.calcular_bolsa():.2f}."
    

# def apresentar_todos(pessoas: list[Pessoa]) -> list[str]:
#     return [p.apresentar() for p in pessoas]


# def main() -> None:
#     p = Pessoa("João", "111.222.333-44")
#     a = Aluno("Ana", "555.666.777-88", "A123")
#     pr = Professor("Carlos", "333.444.555-66", "Matemática")
#     ab = AlunoBolsista("Marcus", "888.999.000-11", "B456")

#     resultados = apresentar_todos([p, a, pr, ab])
#     for r in resultados:
#         print(r)

#     print("\nChecando heranças:")
#     print(f"isinstance(ab, Pessoa): {isinstance(ab, Pessoa)}")
#     print(f"isinstance(ab, Aluno): {isinstance(ab, Aluno)}")
#     print(f"isinstance(ab, BolsaMixin): {isinstance(ab, BolsaMixin)}")

#     print("\nMRO AlunoBolsista:")
#     for cls in AlunoBolsista.__mro__:
#         print(" -", cls.__name__)


# if __name__ == "__main__":
#     main() 