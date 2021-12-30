#Tomorrow's Chopp
<<<<<<< Updated upstream
if __name__ == '__main__':
=======
from Manager_Storage import ManagerEstoque
from Validation_solding import Vendas
from time import sleep

if __name__ == '__main__':
    print("Iniciando Motores!")
    sleep(2)
    print("Insira a quantidade de chopp disponíveis.")
    litros =  float(input())
    sleep(0.5) 
    print("Insira a quantidade de canecas disponíveis.")
    canecas = int(input())
    sleep(0.5)
    estoque_iniciado = ManagerEstoque(litros, canecas)
    print("Maquina Iniciada com sucesso! Tudo pronto para começar")
    while True:
        print("Bem vindo ao Menu Gerencial!")
        print("1°- Iniciar Vendas.")
        print("2°- Inserir mais Chopp.")
        print("3°- Inserir mais canecas.")
        print("4°- Solicitar relatório de vendas.")
        print("5°- Solicitar Fechamento.")
        print("6°- Desligar Maquina!")
        opcao1 = int(input())
        if opcao1 == 6: 
            break

        if opcao1 == 1:
            if litros and canecas > 0:
                while True:
                    senhadegerente = 1707
                    print("Bem vindo ao Tomorrow's Chopp")
                    print("Quantos chopps o senhor(a)deseja?")
                    qnt_chopp_solicitado = int(input())
                    if qnt_chopp_solicitado == 1707:
                        break
                    qnt_canecas = qnt_chopp_solicitado
                    print("Insira o numero do seu cartão")
                    num_cartao = input()
                    saldo_cartao = 100
                    nova_venda = Vendas(qnt_chopp_solicitado, num_cartao, saldo_cartao)
                    estoque_verificado = estoque_iniciado.verificar_estoque(qnt_chopp_solicitado)
                    if estoque_verificado == True:  
                        venda_verificada = nova_venda.VerificarVendas()
                        if venda_verificada == True:
                            nova_venda.RetirarSaldo(qnt_chopp_solicitado)
                            print("Aqui está seu chopp!")
                        else:
                            print("Você não tem dinheiro suficiente.")
                    else:
                        print("Estoque Insuficiente para venda. Favor contatar o gerente.")
            elif opcao1 == 2:
                estoque_iniciado.acrescentar_litros()
            elif opcao1 == 3:
                estoque_iniciado.acrescentar_canecas()
            elif opcao1 == 4:
                print("Em desenvolvimento.")
            elif opcao1 == 5:
                print("Em desenvolvimento.")
            else:
                print("Invalido.")

    
>>>>>>> Stashed changes
