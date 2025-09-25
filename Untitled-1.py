nome = input("Digite o nome do aluno: ")
matricula = input("Digite o número de matrícula: ")
serie = input("Digite a série: ")

nota1 = float(input("Digite a nota do 1° bimestre: "))
nota2 = float(input("Digite a nota do 2° bimestre: "))
nota3 = float(input("Digite a nota do 3° bimestre: "))
nota4 = float(input("Digite a nota do 4° bimestre: "))

print("Por favor, insira um numero válido para as notas.")
media = (nota1 + nota2 + nota3 + nota4) / 4


if media == 6:
    print("Voce está na média")   
elif media >= 4:
    print("Voce está aprovado")
else:
    print("Você está reprovado")

print("/n-- Resultado ---")
print("Nome: ", nome)
print("Número de Matricula: {matricula}")
print("Série: ", serie)
print("Média: ", media)
print("Sua média: ", media)









