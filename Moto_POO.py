class Moto:
    def __init__(self, modelo, ano, cor, marca,cilindradas):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor 
        self.marca = marca
        self.cilindradas = cilindradas

        self.velocidade = 0

    def acelerar(self, valor):
        self.velocidade += valor
        print(f"{self.modelo} acelerou para {self.velocidade} km/h")

    def frear(self, valor):
        self.velocidade -= valor
        if self.velocidade < 0:
            self.velocidade = 0
        print(f"{self.modelo} reduziu para {self.velocidade} km/h.")    

    def detalhes(self):
        return (f"{self.marca}{self.modelo}{self.cilindradas}({self.ano}) - "
                f"Cor: {self.cor}, Velocidade: {self.velocidade} km/h")       
        

moto1 = Moto("Africa twin", "2016", "Branca", "Honda ", " 1100") 
moto2 = Moto("GS", "2024", "Vermelha", "BMW ", " 1300") 

print(moto1.detalhes())
print(moto2.detalhes())

moto1.acelerar(210)
moto2.acelerar(200)

moto1.frear(30)
moto2.frear(50)

