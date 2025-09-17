def carro():
    ano = int(input("Digite o ano do carro: "))
    modelo = input("Digite  o modelo do carro: ")
    cor = input("Digite a cor do carro: ")
   
    print("n--- FICHA DO CARRO ---")     
    print("Seu carro é do ano:", ano)
    print("Seu carro é do modelo:", modelo)
    print("Seu carro é da cor:", cor)
    if ano>2015:
        print("Seu carro é considerado da nova geração segundo a tabela FIP." + )
    else:
        print("Seu carro é considerado da velha geração segundo a tabela FIP." )
carro()    