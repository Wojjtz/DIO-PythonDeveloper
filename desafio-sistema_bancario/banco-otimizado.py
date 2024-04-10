# necessita alterações

import textwrap

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def main():
    LIMITE = 500
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    extratos = "--- Extratos ---"
    numero_saques = 0
    usuarios = []
    contas = []
    numero_contas = 0

    while True:
        opcao = menu()
        
        if opcao == "d":
            valor = float(input("Informe o valor do depósito: R$"))
            depositar(
                saldo_conta=saldo, 
                valor_deposito=valor,
                extratos=extratos
                )

        elif opcao == "s":
            valor = float(input("Informe o valor a ser sacado: R$"))
            sacar(
                saldo_conta=saldo, 
                valor_saque=valor, 
                extratos=extratos
                )
        elif opcao == "e":
            print(extratos)

        elif opcao == "nc":
            numero_contas = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
        elif opcao == "lc":
            listar_contas(contas=contas)
        elif opcao == "nu":
            criar_usuario(usuarios=usuarios)
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

        
def sacar(*saldo_conta, valor_saque, extratos):
    if valor_saque > LIMITE or valor_saque > saldo:
        print("Falha ao realizar saque.")
        adicionar_extrato(resultado="Falha", operacao="saque", valor="0.00")

    else:
        print("Sucesso ao realizar saque.")
        saldo_conta -= valor_saque
        adicionar_extrato(resultado="Sucesso", operacao="saque", valor=valor_saque, extratos=extratos)
    
def depositar(*saldo_conta, valor_deposito, extratos):
    if valor_deposito > 0:
        print("Sucesso ao realizar depósito.")
        saldo_conta += valor_deposito
        adicionar_extrato(resultado="Sucesso", operacao="depósito", valor=valor_deposito, extratos=extratos)

    else:
        print("Falha ao realizar depósito.")
        adicionar_extrato(resultado="Falha", operacao="depósito", valor="0.00")

def adicionar_extrato(*resultado, operacao, valor, extratos):
    extratos += f"{resultado} ao realizar {operacao}. Valor manipulado: R$ {valor:.2f}\n"

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

main()