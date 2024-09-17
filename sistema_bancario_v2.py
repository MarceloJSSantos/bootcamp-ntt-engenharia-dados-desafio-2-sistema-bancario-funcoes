def menu():
    menu = "MENU".center(100, "#") + """

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Nova Usuário
    [5] Novo Conta
    [6] Listar Contas
    [7] Listar usuários
    [0] Sair

    -->"""
    return input(menu)

def deposito(saldo, valor, extrato, /):

    if valor > 0:
        saldo += valor
        extrato += f"DEPÓSITO:\t\tR$ {valor:6.2f}\n"
    else:
        print("O valor informado para depósito não pode ser negativo!")

    return saldo, extrato

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    saldo_induficiente = valor > saldo

    limite_excedido = valor > limite

    numero_saques_excedido = numero_saques >= limite_saques

    if saldo_induficiente:
        print(f"Você não tem saldo suficiente para esse saque. Saldo: R$ {saldo:.2f}")
    elif limite_excedido:
        print(f"O valor do saque é maior que o limite diário. Limite: {limite}")
    elif numero_saques_excedido:
        print(f"Você alcançou o número máximo de saques. Limite: {limite_saques}")
    elif valor > 0:
        saldo -= valor
        extrato += f"SAQUE:\t\t\tR$ {valor*-1:6.2f}\n"
        limite_saques += 1
    else:
        print("O valor informado para saque não pode ser negativo!")

    return saldo, extrato

def exibe_extrato(saldo, /, *, extrato):
    print("EXTRATO".center(100, "="))
    print(extrato)
    print("".center(100, "-"))
    print(f"SALDO:\t\t\t{saldo:6.2f}")
    print("".center(100, "="))

def cria_usuario(usuarios, cpf):
    print("CADASTRO DE USUÁRIO".center(100, "="))
    
    usuario = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    if len(usuario) != 0:
        print(f"O usuário com o CPF: {cpf} já está cadastrado!")
        return
    
    nome = input("Nome completo: ")
    data_nascimento = input("Data de Nascimento (dd/mm/aaaa): ")
    endereco = input("Endereço completo (rua/logradouro, número - bairro - cidade/estado): ")

    usuarios.append({"nome":nome, "data_nascimento":data_nascimento, "cpf":cpf, "endereco":endereco})

def cria_conta(usuarios, contas, cpf):
    print("CADASTRO DE CONTA".center(100, "="))
    
    usuario = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    if len(usuario) != 0:
        numero_conta = str(len(contas) + 1).rjust(8,"0")
        contas.append({"agencia":"0001", "numero_conta":numero_conta, "usuario":usuario[0]})
        return

    print(f"O usuário com o CPF: {cpf} não está cadastrado!\nCadastre-o antes da abertura de Conta!")

def lista_contas(contas):
    print("LISTA DE CONTAS".center(100, "="))
    for conta in contas:
        dados_conta = f"""
            Agência:\t{conta['agencia']}
            Conta:\t{conta['numero_conta']}
            Usuário:\t{conta['usuario']['nome']}
        """
        print("".center(100, "-"))
        print(dados_conta)

def lista_usuarios(usuarios):
    print("LISTA DE USUÁRIOS".center(100, "="))
    for usuario in usuarios:
        dados_usuario = f"""
            Nome:\t{usuario['nome']}
            CPF:\t{usuario['cpf']}
        """
        print("".center(100, "-"))
        print(dados_usuario)

def main():
    saldo = 0
    extrato = ""
    LIMITE_SAQUE_DIARIO = 500
    numero_saques_diario = 0
    LIMITE_NUMERO_SAQUES_DIARIO = 3
    usuarios = []
    contas = []

    while True:
        opcao = int(menu())

        if opcao == 1:
            print("DEPÓSITO".center(100, "#"))
            valor_deposito = float(input("Qual valor você vai depositar? "))
            saldo, extrato = deposito(saldo, valor_deposito, extrato)
        elif opcao == 2:
            print("SAQUE".center(100, "#"))
            valor_saque = float(input("Qual valor você vai sacar? "))
            saldo, extrato = saque(saldo=saldo, valor=valor_saque, extrato=extrato,
                                   limite=LIMITE_SAQUE_DIARIO, numero_saques=numero_saques_diario,
                                   limite_saques=LIMITE_NUMERO_SAQUES_DIARIO)
        elif opcao == 3:
            exibe_extrato(saldo, extrato=extrato)
        elif opcao == 4:
            cpf = input("Informe o CPF (somente números): ")
            cria_usuario(usuarios, cpf)
        elif opcao == 5:
            cpf = input("Informe o CPF (somente números): ")
            cria_conta(usuarios, contas, cpf)
        elif opcao == 6:
            lista_contas(contas)
        elif opcao == 7:
            lista_usuarios(usuarios)
        elif opcao == 0:
            break
        else:
            print("Opção inválida!\nSelecione uma das opções propostas para continuar.")

    print("Obrigado por ser nosso cliente!")

main()