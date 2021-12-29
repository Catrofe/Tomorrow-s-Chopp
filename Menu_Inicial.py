#Menu Inicial da maquina
from time import sleep
from Manager_Storage import Manager_Estoque
from Validation_solding import Vendas
import random

# Menu que inicializa o programa.
class MenuGerencial():
    def start():
        print("Iniciando Motores!")
        sleep(2)
        print("Insira a quantidade de chopp disponíveis.")
        litros =  float(input())
        sleep(0.5) 
        print("Insira a quantidade de canecas disponíveis.")
        canecas = int(input())
        sleep(0.5)
        Manager_Estoque(litros, canecas)
    
#Menu que ira conter o menu gerencial.
    def Menu_Option(self):
        pass

# Menu que realiza a venda.
class MenuVendas:
    @staticmethod
    def menu_init_vendas():
        print("Bem vindo ao Tomorrow's Chopp")
        print("Quantos chopps o senhor(a)deseja?")
        qnt_chopp = int(input())
        print("Insira o numero do seu cartão")
        num_cartao = input()
        saldo_cartao = random.randrange(9,10)
        print("Pedido sendo processado.")
        Vendas(qnt_chopp, num_cartao, saldo_cartao)
        sleep(2)

MenuGerencial.start()


