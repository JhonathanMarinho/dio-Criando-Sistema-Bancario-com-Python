import textwrap

def menu ():
    menu = """

    [d]\t Depositar
    [s]\t Sacar
    [e]\t Extrato
    [nu]\t Novo Usuario
    [nc]\t Nova Conta
    [lc]\t Lista de Contas
    [q]\t Sair

    => """
    return input(textwrap.dedent(menu))

def depositar(saldo,valor,extrato,/):

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: \tR$ {valor:.2f}\n"
        print("\n Deposito realizado com sucesso")
            
    else:
      print("\n Valor invalido para deposito.")
          
    return saldo, extrato 
    
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
        
    excedeu_limite = valor > limite
        
    excedeu_saques = numero_saques >= limite_saques
        
    if excedeu_saldo:
        print("Saldo insuficiente.")
            
    elif excedeu_limite:
        print("saque superior a saldo.")
            
    elif excedeu_saques:
        print("Limite de saque diario atingido")
            
    elif valor > 0:
        saldo -= valor
        extrato += f"saque\t\t R$ {valor:.2f}\n"
        numero_saques += 1
        print(" saque realizado com sucesso. ")
            
    else:
        print("Valor informado invalido.")
        
    return saldo, extrato

def exibir_extrato(saldo,/,*,extrato):
    print("\nNão foram realizadas movimentações." if not extrato else extrato)
    print(f"\n Saldo :\t\t R${saldo:.2f}")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Já existe usuário com esse CPF! ")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] ==cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
    
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usúario: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n Conta criada com sucesso.")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n Usuário não encontrado.")
    
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():    
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []



    while True:
    
        opcao = menu()
    
        if opcao == "d":
            valor = float(input("Digite o valor para deposito. "))
        
            saldo, extrato = depositar(saldo, valor, extrato)
            
        elif opcao == "s":
            valor = float(input("Digite o valor para saque."))
        
            saldo, extrato = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES,
        )
        
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "nu":
            criar_usuario(usuarios)
            
        elif opcao == "nc":
            numero_conta = len(contas)+ 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)
                
        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break
        
        else:
            print("Digite uma opção valida.")
            
            
main()
