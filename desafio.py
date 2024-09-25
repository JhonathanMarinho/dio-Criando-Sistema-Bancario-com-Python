menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3



while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        valor = int(input("Digite o valor para deposito. "))
        
        if valor > 0:
            saldo += valor
            extrato += f"deposito realizado com sucesso :R$ {valor:.2f}\n"
            
        else:
          print("Valor invalido para deposito.")
        
        
    elif opcao == "s":
        valor = float(input("Digite o valor para saque."))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Saldo insuficiente.")
            
        elif excedeu_limite:
            print("saque superior a saldo.")
            
        elif excedeu_saques:
            print("Limite de saque diario atingido")
            
        elif valor > 0:
            saldo -= valor
            extrato += f"saque :R$ {valor:.2f}\n"
            numero_saques += 1
            
        else:
            print("Valor informado invalido.")
        
    elif opcao == "e":
        print("\nNão foram realizadas movimentações." if not extrato else extrato)
        print(f"\n Saldo : R${saldo:.2f}")
        
    elif opcao == "q":
        break
        
    else:
        print("Digite uma opção valida.")