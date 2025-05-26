class Cachorro:
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca

    def latir(self):
        print(f"Au au! Eu sou o {self.nome}, da raça {self.raca}.")

c1 = Cachorro("Bolt", "Pastor Alemão")
c2 = Cachorro("Totó", "Poodle")
c3 = Cachorro("Max", "Labrador")

c1.latir()
c2.latir()
c3.latir()