menu = """
========== $$$ ==========

    [1] Sacar 
    [2] Depositar
    [3] Extrato
    [0] Sair

=========================
R: 
"""

saldo = 0
extrato = """
=============================

        Extratos
        
=============================
"""
numero_saques = 0
LIMITE = 500
LIMITE_SAQUES = 3

while numero_saques <= LIMITE_SAQUES:
    opcao = input(menu)
    mensagem = ""

    if opcao == "1":

        resultado_saque = ""

        valor_saque = float(input("Valor a sacar: R$ "))

        if(valor_saque > LIMITE or valor_saque > saldo):
            resultado_saque = "Falha"
            
        else:
            resultado_saque = "Sucesso"
            saldo -= valor_saque
            numero_saques += 1
            
        mensagem =f"""
=============================
                    
{resultado_saque} ao realizar
o saque.

Saque: R$ {valor_saque:.2f}               
Saldo: R$ {saldo:.2f}
                
=============================
"""
    elif opcao == "2":
        resultado_deposito = ""

        valor_deposito = float(input("Valor a depositar: R$ "))

        if(valor_deposito > 0):
            saldo += valor_deposito
            resultado_deposito = "Sucesso"
        else:
            resultado_deposito = "Falha"

        mensagem = f"""
=============================

{resultado_deposito} ao realizar
o deposito.

Deposito: R$ {valor_deposito:.2f}               
Saldo: R$ {saldo:.2f}
            
=============================
"""
    elif opcao == "3":
        print(extrato)
    elif opcao == "0":
        break
    else: 
        print("""
===================================================
              
Operação inválida. Por favor, selecione novamente.
              
===================================================
""")
    
    extrato += mensagem
    print(mensagem)

print("""
====================================
      
Obrigado por utilizador nosso banco! 
      
====================================    
""")


