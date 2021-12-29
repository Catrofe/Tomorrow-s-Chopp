# from Validation_solding import Validation

# Classe que gerencia o estoque.
class Manager_Estoque():
    def __init__(self, litros, canecas):
        self.litros = litros
        self.canecas = canecas

# Função que acrescenta litros.
    def AcrescentarLitros(self):
        print("Quantos litros deseja acrescentar?")
        varlitros = float(input())
        self.litros = varlitros + litros
        return self.litros
    
# Função que acrescenta canecas.
    def AcrescentarCanecas(self):
        print("Quantos canecas deseja acrescentar?")
        varcanecas = int(input())
        self.litros = varcanecas + litros
        return self.canecas

# Função que remove o estoque após a venda.
    def VendaExecutada(self, qnt_litros, qnt_canecas):
        self.litros -=  qnt_litros
        self.canecas -= qnt_canecas 

# Manager_Estoque(litros, canecas)

# Manager_Estoque.VendaExecutada(0.5, 1)