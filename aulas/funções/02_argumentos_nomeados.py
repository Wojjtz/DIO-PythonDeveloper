def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


salvar_carro("Fiat", "Palio", 1999, "ABC-1234") # o usuário pode trocar os argumentos, gerando erros
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234") # adiciona independente da ordem
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"}) # ** = adiciona um dicionário 