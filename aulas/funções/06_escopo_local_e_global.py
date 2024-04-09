# Dentro do bloco da função o escopo é local, alterações ali feitas em objetos imutáveis seráo perdidas quando o método terminar

salario = 2000

def salario_bonus(bonus):
    global salario # informa que a variavel é global
    salario += bonus
    return salario

salario_bonus(500)  # 2500

# Essa NÃO É uma boa prática e deve ser evitada