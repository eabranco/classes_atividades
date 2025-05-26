class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def comprar(self, qtd):
        if qtd <= self.estoque:
            self.estoque -= qtd
            print(f"{qtd} unidade(s) de {self.nome} comprada(s).")
        else:
            print(f"Estoque insuficiente! Apenas {self.estoque} unidade(s) disponíveis.")

    def repor(self, qtd):
        self.estoque += qtd
        print(f"{qtd} unidade(s) de {self.nome} adicionada(s) ao estoque.")

    def mostrar_estoque(self):
        print(f"Estoque atual de {self.nome}: {self.estoque} unidade(s)")

p1 = Produto("Caneta", 2.50, 10)

p1.mostrar_estoque()
p1.comprar(5)
p1.mostrar_estoque()
p1.comprar(10)  # Tentativa de compra acima do estoque
p1.repor(20)
p1.mostrar_estoque()
