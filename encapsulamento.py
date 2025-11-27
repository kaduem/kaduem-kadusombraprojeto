# class Conta:
#     def __init__(self, saldo = 0):
#         self.__saldo = saldo

#     @property
#     def saldo(self):
#         return self.__saldo

#     @saldo.setter

#     def saldo(self, valor):
#      if valor >= 0:
#         self.__saldo = valor
#      else:
#         print("Saldo não pode ser negativo.")

#     def depositar (self, valor):
#         if valor > 0:
#             self.__saldo += valor
        
# conta2 = Conta(500)
# print("Saldo inical:", conta2.saldo)

# conta2.saldo = -300
# print("Saldo após tentativa externa:" , conta2.saldo)

# conta2.depositar(300)
# print("Saldo após deposito:" , conta2.saldo)

class Aluno:
    def __init__(self, nota = 0):
        self.__nota = nota

    @property
    def nota(self):
        return self.__nota

    @nota.setter
    
    def nota(self, valor):
     if valor >= 0:
        self.__nota = valor
     else:
        print("Nota não pode ser negativa.")
    def ingressar(self, valor):
        if valor > 0:
            self.__nota += valor
        
aluno1 = Aluno(600)
print("Nota inicial:", aluno1.nota)

#aluno1.nota = -300
#print("Nota após tentativa externa:" , aluno1.nota)

aluno1.ingressar(230)
print("Nota após corte:" , aluno1.nota)