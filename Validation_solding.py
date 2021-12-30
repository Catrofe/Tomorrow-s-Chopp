#Essa parte irá verificar se o cartão possui crédito. Caso sim, ela irá efetuar a compra e retirar saldo. Caso não irá negar a compra.
<<<<<<< Updated upstream

def Validation():

    productValue = 5
    transation = None

    if credito == productValue or credito > productValue:
        NewCredit = credito - productValue
        credito = NewCredit
        transation = True

    else:
        print("Saldo Insuficiente.")
        transation = False
    return transation









=======
from Manager_Storage import ManagerEstoque



# Classe que cuida dos componetes financeiros/vendas.
class Vendas():
    def __init__(self, qnt_chopp, num_cartao, saldo_cartao):
        self.qnt_chopp = qnt_chopp
        self.num_cartao = num_cartao
        self.saldo_cartao = saldo_cartao

# Verifica se existe saldo e se sim efetua o pagamento e libera o chopp para o cliente.
    def VerificarVendas(self):
        valor_devido = self.qnt_chopp * 8
        qnt_chopp_litro = self.qnt_chopp * 0.5
        if self.saldo_cartao > valor_devido:
            return True
        return False
    
    def RetirarSaldo(self, valor_devido):
        self.valor_devido = valor_devido * 8
        self.saldo_cartao -= valor_devido
        


                    # manager = ManagerEstoque(100.0, 100)
            # manager.VendaExecutada(qnt_chopp_litro, self.qnt_chopp)
>>>>>>> Stashed changes
