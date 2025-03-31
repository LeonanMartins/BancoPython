menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:

    opcao = input(menu)
    
    if opcao == 1:
        valor = float(input('Digite o valor do depósito: '))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"        

        else:
            print('Operação não realizada, por favor digite um valor válido')
        
    
    elif opcao == 2:
        valor = float(input('Digite o valor do saque: '))
        exedeu_saldo = valor > saldo
        exedeu_limite = valor >= limite
        exedeu_saques = numero_saques >= limite_saques

        if exedeu_saldo:
            print('Saldo Insuficiente')

        elif exedeu_limite:
            print('Limite de saques atingido')

        elif exedeu_saques:
            print('Limite de saques atingido')
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print('Operação não realizada, por favor digite um valor válido')
        
    
    elif opcao == 3:        
        print("\n===============Extrato===============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=======================================")
    
    elif opcao == 4:
        break
    
    else:
        print('Opção inválida, por favor selecione uma opção válida')
