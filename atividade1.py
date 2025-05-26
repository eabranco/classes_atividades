class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

p1 = Pessoa("Ewerton", 48)
p2 = Pessoa("Mari", 26)
p1.apresentar()
p2.apresentar()