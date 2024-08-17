import re
from validate_docbr import CNPJ, CPF

def cpf_invalido(num_cpf):
    cpf = CPF()
    cpf_valido = cpf.validate(num_cpf)
    return not cpf_valido


def cnpj_invalido(num_cnpj):
    cnpj = CNPJ()
    cnpj_valido = cnpj.validate(num_cnpj)
    return not cnpj_valido


def nome_invalido(nome):
    return not nome.isalpha()


def celular_invalido(celular):
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, celular)
    return not resposta