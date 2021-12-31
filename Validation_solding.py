# Classe que cuida dos componetes financeiros/vendas.
class Vendas():
    def __init__(self, qnt_chopp, num_cartao):
        self.qnt_chopp = qnt_chopp
        self.num_cartao = num_cartao
        saldo_cartao = 10000
        self.saldo_cartao = saldo_cartao

# Verifica se existe saldo e se sim efetua o pagamento e libera o chopp para o cliente.
    def VerificarVendas(self):
        valor_devido = self.qnt_chopp * 8
        qnt_chopp_litro = self.qnt_chopp * 0.5
        if self.saldo_cartao > valor_devido:
            self.saldo_cartao -= valor_devido
            return True
        return False
    
    # def RetirarSaldo(self, valor_devido):
    #     self.valor_devido = valor_devido * 8
    #     self.saldo_cartao -= valor_devido
        
    

                    # manager = ManagerEstoque(100.0, 100)
            # manager.VendaExecutada(qnt_chopp_litro, self.qnt_chopp)
