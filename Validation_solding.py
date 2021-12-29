#Essa parte irá verificar se o cartão possui crédito. Caso sim, ela irá efetuar a compra e retirar saldo. Caso não irá negar a compra.
from Manager_Storage import Manager_Estoque



# Classe que cuida dos componetes financeiros/vendas.
class Vendas():
    def __init__(self, qnt_chopp, num_cartao, saldo_cartao):
        self.qnt_chopp = qnt_chopp
        self.num_cartao = num_cartao
        self.saldo_cartao = saldo_cartao
        
        Vendas.VerificarVendas(self)

# Verifica se existe saldo e se sim efetua o pagamento e libera o chopp para o cliente.
    def VerificarVendas(self):
        preco_produto = 8

        valor_devido = self.qnt_chopp * preco_produto
        qnt_chopp_litro = self.qnt_chopp * 0.5
        if self.saldo_cartao > valor_devido:
            manager = Manager_Estoque(100.0, 100)
            manager.VendaExecutada(qnt_chopp_litro, self.qnt_chopp)
            # Manager_Estoque.VendaExecutada(self, qnt_chopp_litro, self.qnt_chopp)
            print("Compra Aprovada. Vou preparar seu chopp.")
        else:
            print ("Você não tem saldo suficiente.")
        
        


























































# def Validation():

#     productValue = 5
#     transation = None

#     if credito == productValue or credito > productValue:
#         NewCredit = credito - productValue
#         credito = NewCredit
#         transation = True

#     else:
#         print("Saldo Insuficiente.")
#         transation = False
#     return transation