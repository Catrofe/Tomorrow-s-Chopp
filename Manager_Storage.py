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




