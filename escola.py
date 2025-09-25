
def secretaria():
    print("Bem-Vindo à Escola Aprendiz Indicador")
    nome=input("Qual seu nome: ")
    idade=int(input("Qual sua idade: "))
    
    escm =int(input( "Digite 1 caso você seja um professor, digite 2 para aluno, digite 3 se você for zelador: "))
    def professor():
        if escm ==1:
            escprof= int(input("----------------------------------\nDigite 1 caso você queira lançar notas\nDigite 2 para ver suas turmas"
        "\nDigite 3 para horario escolar")) 
            
            if escprof ==1:
                na = input("Digite o nome do aluno: ")
                se = input("Digite a serie do aluno: ")
                mat= input("digite a materia:")
                n1=int(input("digite a primeira nota do ano: ")) 
                n2=int(input("digite a segunda nota do ano: ")) 
                n3=int(input("digite a terceira nota do ano: ")) 
                n4=int(input("digite a quarta nota do ano: "))
                def media():

                    sn = (n1+n2+n3+n4)/4
                    if sn>6:
                        print("A media do ",na," de ",se," é",sn,", a sua situação atual é APROVADO.")
                    else:
                        print("A media do ",na," de ",se," é",sn,", a sua situação atual é REPROVADO.")
                media()        
            if escprof == 2:
                print("você está responsavel pelas turmas Ds1, Ds2, Ds3")
            if escprof == 3:
                print("07h30 - 08h00: Chegada dos alunos, atividades livres \n" 
                "08h00 - 09h40:Aulas de Línguagem de Programação Bloco 1. \n" 
                "09h40 - 10h00:Intervalo para lanche.\n" 
                "10h00 - 11h40:Aulas de Gestão de Startup Bloco 2. \n"
                "11h40 - 12h00:Preparação para o almoço.\n"
                "Tarde:\n"
                "12h00 - 13h00:Almoço e descanso.\n"
                "13h00 - 14h40:Aulas de Redes de computadores Bloco 3.\n"
                "14h40 - 15h00:Intervalo.\n1"
                "15h00 - 16h40:Atividades Extracurriculares: aulas de informática, robótica ou aulas de inglês. ")


                
                 
    def aluno():       
        if escm ==2:
            escalu= int(input("----------------------------------\nDigite 1 caso você queira reservar livro:\nDigite 2 para ver o cardapio da semana: " \
        "\nDigite 3 para solicitar declaração"))
            if escalu == 1:
                n1=int(input("digite a primeira nota do ano: ")) 
                n2=int(input("digite a segunda nota do ano: ")) 
                n3=int(input("digite a terceira nota do ano: ")) 
                n4=int(input("digite a quarta nota do ano: "))

                sn = (n1+n2+n3+n4)/4
                if sn>6:
                    print("Sua media",sn," situação atual é APROVADO.")
                else:
                    print("Sua media",sn," situação atual é REPROVADO.")
                
            if escalu == 2:
                print("---------------------\nSegunda-feira: Sopa de legumes com carne, acompanhada de pão integral.\n"
"Terça-feira: Arroz com lentilha e frango ao molho.\n"
"Quarta-feira: Macarrão com atum e salada colorida.\n"
"Quinta-feira: Feijão, arroz, bife de carne moída e salada de folhas."
"Sexta-feira: Peixe frito com pirão e salada de legumes.")
                
            if escalu==3:
                nr = input("Digite o nome do seu responsável: ")
                n = input("Digite o seu nome: ")
                print("Declaramos, para os devidos fins, que o(a) ",nome,", está regularmente matriculado(a) na Escola Aprendiz Indicador"
                "Esta declaração é emitida para finalidade, ex: comprovação de matrícula, apresentação em órgãos competentes, etc., e tem validade até de até 3 dias"
                "\nAv.J 1770, 05 de Setembro."
                "\nAprendiz Indicador")
    def zelador():
        esczel = int(input("Digite 1 se você quiser verificar estoque, digite 2 se você quiser adicionar material"))
        materiais = {
                "esponjas": 10,
                "sacos de lixo": 50,
                "lâmpadas" :25
            }
        if esczel == 1:
            materiais = {"esponjas": 5, "panos": 10, "sacos de lixo": 20}
            print(materiais)

        if esczel == 2:
            
            
            def adicionar_material(nome_material, quantidade):
                nome_material = input("Digite o nome do material que voce queira adicionar: ")
                quantidade = input("Digite a quantidade: ")
                if nome_material in materiais:
                    materiais[nome_material] += quantidade 
                else:
                    materiais[nome_material] = quantidade
                    print(f"{quantidade}{nome_material} adicionados a. Total {materiais[nome_material]}")
            def mostrar_materiais():
                print("Lista de Materiais")
                for material, quantidade in materiais.items():
                    print(f"{material}:{quantidade}")
            adicionar_material("nome_material", "quantidade")
            mostrar_materiais()






    professor()
    aluno()
    zelador()
secretaria()

git config --global user.email "kaduemanuel7@gmail.com"
git config --global user.name "kaduem"