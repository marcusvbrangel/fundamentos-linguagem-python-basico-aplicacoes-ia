
from entidades.cliente import Cliente
from entidades.conta import Conta, ContaCorrente, ContaPoupanca
from utilitarios.exceptions import ContaInexistenteError, ClienteInexistenteError, TipoContaInvalidaError

class Banco:

    """
    Gerencia as operacoes do banco
    """

    def __init__(self, nome: str):

        self.nome = nome

        # dicionario de clientes (chave: cpf, valor: objeto Cliente)
        self._clientes = {}

        # dicionario de contas (chave: numero da conta, valor: objeto Conta)
        self._contas = {}

    def adicionar_cliente(self, nome: str, cpf: str) -> Cliente:

        if cpf in self._clientes:
            print("Erro: Cliente com este CPF já cadastrado")
            return self._clientes[cpf]
        
        novo_cliente = Cliente(nome, cpf)
        self._clientes[cpf] = novo_cliente

        print(f"Cliente {nome} adicionado com sucesso.")

        return novo_cliente
    
    def buscar_cliente(self, cpf: str) -> Cliente:

        cliente = self._clientes.get(cpf)

        if not cliente:
            raise ClienteInexistenteError(cpf)
        
        return cliente

    def criar_conta(self, cliente: Cliente, tipo: str) -> Conta:

        numero_conta = Conta.get_total_contas() + 1

        if tipo.lower() == 'corrente':
            nova_conta = ContaCorrente(numero_conta, cliente)

        elif tipo.lower() == 'poupanca':
            nova_conta = ContaPoupanca(numero_conta, cliente)

        else:
            print("Tipo de conta inválido. Escolha 'corrente' ou 'poupanca'.")
            raise TipoContaInvalidaError("Tipo de conta inválida.")
        
        self._contas[numero_conta] = nova_conta
        cliente.adicionar_conta(nova_conta)
        print(f"Conta: {tipo} Nº {numero_conta} criada para o cliente {cliente.nome}")

        return nova_conta
    
    def buscar_conta(self, numero_conta: int) -> Conta:

        conta = self._contas.get(numero_conta)

        if not conta:
            raise ContaInexistenteError(numero_conta)
        
        return conta
            
