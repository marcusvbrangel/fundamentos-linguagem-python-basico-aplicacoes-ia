
from operacoes.banco import Banco
from utilitarios.exceptions import ContaInexistenteError, SaldoInsuficienteError

def menu_principal():

    print("\n--- Sistema Bancário ---\n")
    print("1. Adicionar Cliente")
    print("2. Criar Conta")
    print("3. Acessar Conta")
    print("4. Sair\n")

    return input("Escolha um opção: ")


def menu_conta(banco: Banco):
    pass


def main():
    pass


# ponto de entrada da aplicacao
if __name__ == "__main__":
    main()
