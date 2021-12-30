<<<<<<< Updated upstream
# from Validation_solding import Validation

valorCartao = 100
VALORPRODUTO = 5



def InicializarEstoqueLitros():
    print("Insira a quantidade de chopp disponíveis.")
    litros =  float(input())
    return litros


def InicializarEstoqueCanecas():
    print("Insira a quantidade de canecas disponíveis.")
    canecas = int(input())
    return canecas


def ConfereEstoque(litros, canecas):
    if litros >= 0.5 and canecas >= 1:
        return True
    return False


def Validation(estoque):
    global valorCartao
    if estoque: 
        if  valorCartao >= VALORPRODUTO:
            valorCartao = valorCartao - VALORPRODUTO
            return True
    print("Saldo Insuficiente.")
    return False


def LiberarProduto():
    EstoqueInitLitros = InicializarEstoqueLitros()
    EstoqueInitCanecas = InicializarEstoqueCanecas()

    estoqueConferido = ConfereEstoque(EstoqueInitLitros, EstoqueInitCanecas)
    produtoValidado =  Validation(estoqueConferido)

    if estoqueConferido and produtoValidado:
        EstoqueInitLitros = EstoqueInitLitros - 0.5
        EstoqueInitCanecas = EstoqueInitCanecas - 1
        print("Aproveite seu chopp. Volte sempre.")
    else:
        print("Algo deu errado. Estou acionando o gerente.")
    print(EstoqueInitLitros, EstoqueInitCanecas)

LiberarProduto()



=======
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
        if litros_utilizados < self.litros:
            if canecas_utilizadas < self.canecas:
                return True
        return False

# Função que remove o estoque após a venda.
    def venda_executada(self, qnt_litros, qnt_canecas):
        self.litros -=  qnt_litros
        self.canecas -= qnt_canecas
>>>>>>> Stashed changes

