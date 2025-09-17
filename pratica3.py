def cadastro():
    nome = input("Digite seu nome: ")
    cpf = input("Digite seu cpf: ")
    endereco = input("Digite o seu endereço: ")
    idade = int(input("Digite sua idade:"))
   
    print("n--- FICHA DE CADASTRO ---")     
    print("Meu nome é:", nome)
    print("Meu cpf é:", cpf)
    print("Meu endereço é:", endereco)
    if idade<18:
        print("Você é menor de idade, não pode se cadastrar.")
    else:
        print("Você é maior de idade, \nCadastro concluído com sucesso." )
cadastro()    