def valida_cpf(num_cpf):
    if len(num_cpf) != 11:
        return False
    if num_cpf.count(num_cpf[0]) == len(num_cpf):
        return False

    soma = 0
    for i in range(9):
        soma += int(num_cpf[i]) * (10 - i)
    resto = 11 - (soma % 11)
    if resto == 10 or resto == 11:
        digito1 = 0
    else:
        digito1 = resto

    soma = 0
    for i in range(10):
        soma += int(num_cpf[i]) * (11 - i)
    resto = 11 - (soma % 11)
    if resto == 10 or resto == 11:
        digito2 = 0
    else:
        digito2 = resto
    if digito1 != int(num_cpf[9]) or digito2 != int(num_cpf[10]):
        return False

    return True

def valida_cnpj(cnpj):
    if len(cnpj) != 14:
        return False

    def calcula_digito(cnpj, multiplicadores):
        soma = sum(int(cnpj[i]) * multiplicadores[i] for i in range(len(multiplicadores)))
        resto = soma % 11
        return '0' if resto < 2 else str(11 - resto)

    multiplicadores_1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    multiplicadores_2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    primeiro_digito = calcula_digito(cnpj[:12], multiplicadores_1)
    segundo_digito = calcula_digito(cnpj[:12] + primeiro_digito, multiplicadores_2)
    return cnpj[-2:] == primeiro_digito + segundo_digito