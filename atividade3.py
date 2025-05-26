class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self.velocidade = 0  # Velocidade começa em 0

    def acelerar(self):
        self.velocidade += 10

    def frear(self):
        self.velocidade = max(0, self.velocidade - 10)  # Não permite velocidade negativa

    def mostrar_velocidade(self):
        print(f"Velocidade atual do {self.modelo}: {self.velocidade} km/h")

carro1 = Carro("Fusca")

carro1.mostrar_velocidade()
carro1.acelerar()
carro1.acelerar()
carro1.mostrar_velocidade()
carro1.frear()
carro1.mostrar_velocidade()
carro1.frear()
carro1.frear()  # Testando para não ir abaixo de 0
carro1.mostrar_velocidade()
