
from decimal import Decimal, InvalidOperation
from operacoes.banco import Banco
from utilitarios.exceptions import (
    ContaInexistenteError, 
    SaldoInsuficienteError, 
    ClienteInexistenteError, 
    TipoContaInvalidaError
)

# funcao que exibe o menu principal da aplicacao
def menu_principal():

    print("\n--- Sistema Bancário ---\n")
    print("1. Adicionar Cliente")
    print("2. Criar Conta")
    print("3. Acessar Conta")
    print("4. Sair\n")

    return input("Escolha um opção: ")


# funcao que exibe o menu de operacoes de uma conta especifica
def menu_conta(banco: Banco):

    try:

        # solicita ao usuario o numero da conta
        numero_conta = int(input("Digite o número da conta: "))

        # busca a conta
        conta = banco.buscar_conta(numero_conta)

        # loop de operacoes dentro da conta
        while True:

            print(f"\n--- Operações para Conta Nº {conta.numero} ---")
            print(f"Cliente: {conta.cliente.nome} | Saldo: R${conta.saldo:.2f}")
            print("1. Depositar")
            print("2. Sacar")
            print("3. Ver Extrato")
            print("4. Voltar ao Menu Principal")

            # le a opcao do usuario
            opcao = input("Escolha uma opção: ")

            if opcao == '1':

                try:

                    # deposita valor na conta
                    valor = Decimal(input("Digite um valor para depósito: ")).replace(",", '.')
                    conta.depositar(valor)

                except InvalidOperation:
                    print("Erro: valor monetário inválido.")

            elif opcao == '2':

                # tenta realizar um saque
                try:

                    valor = Decimal(input("Digite um valor para saque: ")).replace(",", ".")
                    conta.sacar(valor)

                except InvalidOperation:
                    print("Erro: valor monetário inválido.")

                except SaldoInsuficienteError as e:
                    print(f"Erro na operação: {e}")

            elif opcao == '3':

                # exibe o extrato da conta
                conta.exibir_extrato()

            elif opcao == '4':

                # sai do menu da conta e retorna ao menu principal
                break

            else:
                print("Opção inválida. Tente novamente")

    # excecao caso a conta nao exista
    except ContaInexistenteError as e:
        print(f"Erro: {e}")

    # excecao para entradas invalidas (nao numericas)
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um número")


# funcao principal que controla o fluxo do sistema
def main():

    banco = Banco("Banco Digital")

    while True:

        opcao = menu_principal()

        if opcao == '1':

            # adiciona um novo cliente
            nome = input("Digite o nome do cliente: ").strip()
            cpf = input("Digite o CPF do cliente: ").strip()
            
            if not nome or not cpf:
                print("Nome ou CPF não pode ser vazio.")
                continue

            banco.adicionar_cliente(nome, cpf)

        elif opcao == '2':

            cpf = input("Digite o CPF do cliente para vincular a conta: ").strip()

            try:

                cliente = banco.buscar_cliente(cpf)

                tipo_conta = input("Digite o tipo da conta: (corrente/poupanca): ").strip().lower()
                banco.criar_conta(cliente, tipo_conta)

            except ClienteInexistenteError as e:
                print(f"Erro: {e}")

            except TipoContaInvalidaError as e:
                print(f"Erro: {e}")

        elif opcao == '3':

            # abre o menu de operacoes de uma conta
            menu_conta(banco)

        elif opcao == '4':

            # encerra o programa
            print("\nObrigado por usar o nosso sistema")
            break

        else:
            print("\nOpção inválida. Por favor, tente novamente\n")



# ponto de entrada da aplicacao
if __name__ == "__main__":
    main()
