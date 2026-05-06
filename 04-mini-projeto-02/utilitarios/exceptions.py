
class SaldoInsuficienteError(Exception):

    """
    Excecao disparada quando uma operacao de saque excede o saldo disponivel
    """

    def __init__(self, saldo_atual, valor_saque, mensagem="Saldo insuficiente para realizar o saque."):
        self.saldo_atual = saldo_atual
        self.valor_saque = valor_saque
        self.mensagem = f"{mensagem} Saldo atual: R${saldo_atual:.2f}, tentativa de saque: R${valor_saque:.2f}"
        super().__init__(self.mensagem)


class ContaInexistenteError(Exception):

    """
    Excecao disparada ao tentar operar uma conta inexistente
    """

    def __init__(self, numero_conta, mensagem="A conta especificada não foi encontrada."):
        self.numero_conta = numero_conta
        self.mensagem = f"{mensagem} Número da conta: {numero_conta}"
        super().__init__(self.mensagem)


class ClienteInexistenteError(Exception):

    """
    Excecao disparada ao tentar buscar um cliente inexistente
    """

    def __init__(self, cpf: str, mensagem="O cliente especificado não foi encontrado."):
        self.cpf = cpf
        self.mensagem = f"{mensagem} CPF: {cpf}"
        super().__init__(self.mensagem)


class TipoContaInvalidaError(Exception):

    """
    Excecao disparada ao tentar informar um tipo de conta invalida
    """

    def __init__(self, mensagem="Tipo de conta inválida."):
        self.mensagem = f"{mensagem}"
        super().__init__(self.mensagem)

