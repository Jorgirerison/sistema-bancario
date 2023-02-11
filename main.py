menu = '''
   
    [d] Depósito
    [s] Saque
    [e] Extrato
    [q] Sair

=> '''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor = float(input("Digite o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito R$ {valor:.2f}\n"

        else:
            print("Operação falhou! Valor informado é inválido.")

    elif opcao == 's':
        valor = float(input("Digite o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques > LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! O limite de saques foi atingido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! Valor informado é inválido.")

    elif opcao == 'e':
        print(" Extrato ".center(31, "="))
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("".center(31, "="))

    elif opcao == 'q':
        break

    else:
        print("Opção inválida! Por favor selecione novamente a operação desejada.")
