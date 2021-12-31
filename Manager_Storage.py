
# from Validation_solding import Validation
# Classe que gerencia o estoque.
class ManagerEstoque():
    def __init__(self, litros, canecas):
        self.litros = litros
        self.canecas = canecas

# Função que acrescenta litros.
    def acrescentar_litros(self):
        print("Quantos litros deseja acrescentar?")
        varlitros = float(input())
        self.litros += varlitros
        print(self.litros)
    
# Função que acrescenta canecas.
    def acrescentar_canecas(self):
        print("Quantos canecas deseja acrescentar?")
        varcanecas = int(input())
        self.canecas += varcanecas
        print(self.canecas)

    #Ele pedia o self, pois eu inicia a classe e depois chamava outra classe. e ele não sabia em que classe procurar.
    def verificar_estoque(self, litros_solicitados): 
        self.litros_solicitados = litros_solicitados
        litros_utilizados = self.litros_solicitados * 0.5
        canecas_utilizadas = self.litros_solicitados
        if litros_utilizados <= self.litros:
            if canecas_utilizadas <= self.canecas:
                return True
        return False

# Função que remove o estoque após a venda.
    def venda_executada(self):
        self.canecas -= self.litros_solicitados
        self.litros -= self.litros_solicitados * 0.5

        # self.litros -=  qnt_litros
        # self.canecas -= qnt_canecas

