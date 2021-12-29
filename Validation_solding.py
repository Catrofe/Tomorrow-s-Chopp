#Essa parte irá verificar se o cartão possui crédito. Caso sim, ela irá efetuar a compra e retirar saldo. Caso não irá negar a compra.

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









