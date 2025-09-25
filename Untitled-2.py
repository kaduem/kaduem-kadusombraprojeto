import datetime

def validar_idade(data_nascimento):
    # Converte a string da data de nascimento para um objeto datetime
    data_nascimento = datetime.datetime.strptime(data_nascimento, "21/12/2007")
    # Data atual
    data_atual = datetime.datetime.today()
    # Calcula a diferença de anos
    idade = data_atual.year - data_nascimento.year
    # Se ainda não fez aniversário este ano, subtrai 1
    if data_atual.month < data_nascimento.month or (data_atual.month == data_nascimento.month and data_atual.day < data_nascimento.day):
        idade -=1
    return idade

def cadastrar_titulo_eleitor():
    print("Cadastro de Título de Eleitor")

    # Solicitar dados do usuário
    nome = input("Digite seu nome: ")
    numero_titulo = input("Digite o número do título de eleitor (somente números): ")
    data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
    
    try:
        idade = validar_idade(data_nascimento)
        if idade < 16:
            print(f"Você ainda não tem idade suficiente para votar. Idade: {idade} anos.")
            return
    except ValueError:
        print("Formato de data inválido! Utilize o formato dd/mm/aaaa.")
        return

    zona = input("Digite o número da zona eleitoral: ")
    secao = input("Digite o número da seção eleitoral: ")
    
    # Exibir os dados cadastrados
    print("\n--- Cadastro Realizado ---")
    print(f"Nome: {nome}")
    print(f"Número do Título: {numero_titulo}")
    print(f"Data de Nascimento: {data_nascimento}")
    print(f"Idade: {idade} anos")
    print(f"Zona Eleitoral: {zona}")
    print(f"Seção Eleitoral: {secao}")
    
    # Determina se o eleitor pode votar
    if idade >= 16:
        print("Status: Você está apto a votar!")
    else:
        print("Status: Você ainda não está apto a votar.")

# Chama a função de cadastro
cadastrar_titulo_eleitor()