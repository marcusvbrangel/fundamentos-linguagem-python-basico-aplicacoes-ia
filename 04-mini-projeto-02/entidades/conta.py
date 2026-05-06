
from abc import ABC, abstractmethod
from datetime import datetime
from decimal import Decimal
from utilitarios.exceptions import SaldoInsuficienteError
from entidades.cliente import Cliente

#-------------------------------------------------------------
# ---------- conta base --------------------------------------

class Conta(ABC):

    """
    Classe base abstrata para contas bancarias
    """

    _total_contas = 0

    def __init__(self, numero: int, cliente: Cliente):

        self._numero: int = numero
        self._saldo: Decimal = Decimal("0.00")
        self._cliente: Cliente = cliente
        self._transacoes = []
        Conta._total_contas += 1


    # getter para o saldo, permitindo acesso controlado
    @property
    def saldo(self) -> Decimal:
        return self._saldo

    @property
    def numero(self) -> int:
        return self._numero
    
    @property
    def cliente(self) -> Cliente:
        return self._cliente
    
    @classmethod
    def get_total_contas(cls):
        return cls._total_contas
    
    def depositar(self, valor: Decimal):

        if valor > 0:
            self._saldo += valor
            self.registrar_transacao(valor, "Depósito")
            print(f"Depósito de R${valor:.2f} realizado com sucesso")
        else:
            print("Valor de depósito inválido") 

    def registrar_transacao(self, valor: Decimal, tipo_transacao: str):
        self._transacoes.append((datetime.now(), f"{tipo_transacao} de R${valor:.2f} | Saldo: R${self._saldo:.2f}"))

    @abstractmethod
    def sacar(self, valor: float):
        pass

    def exibir_extrato(self):

        print(f"\n--- Extrato da Conta Nº {self._numero} ---")
        print(f"Cliente: {self._cliente.nome}")
        print(f"Saldo atual: R${self._saldo:.2f}")

        if not self._transacoes:
            print("Nenhuma transação registrada")
        
        for data, transacao in self._transacoes:
            print(f"- {data.strftime('%d/%m/%Y %H:%M:%S')}: {transacao}")

        print("--------------------------------------\n")

    def __str__(self):
        return f"Conta Nº {self._numero} | Cliente: {self._cliente.nome} | Saldo: R${self._saldo:.2f}"



#-------------------------------------------------------------
# ---------- conta corrente ----------------------------------

class ContaCorrente(Conta):

    def __init__(self, numero: int, cliente: Cliente, limite: Decimal | None = None):

        super().__init__(numero, cliente)
        self.limite = limite if limite is not None else Decimal("500.00")

    def sacar(self, valor: Decimal):

        if valor <= 0:
            print("Valor de saque inválido")
            return
        
        saldo_disponivel = self._saldo + self.limite

        if valor > saldo_disponivel:
            raise SaldoInsuficienteError(saldo_disponivel, valor, "Saldo e limite insuficientes.")

        self._saldo -= valor

        self.registrar_transacao(valor, "Saque")
        print(f"Saque de R${valor:.2f} realizado com sucesso.")

    def __str__(self):
        return f"Conta Corrente Nº {self._numero} | Saldo: R${self._saldo:.2f} | Limite: R${self.limite:.2f}"



#-------------------------------------------------------------
# ---------- conta poupanca ----------------------------------

class ContaPoupanca(Conta):

    def __init__(self, numero: int, cliente: Cliente):

        super().__init__(numero, cliente)
    
    def sacar(self, valor: Decimal):

        if valor <= 0:
            print("Valor de saque inválido")
            return
        
        if valor > self._saldo:
            raise SaldoInsuficienteError(self.saldo, valor)

        self._saldo -= valor

        self.registrar_transacao(valor, "Saque")
        print(f"Saque de R${valor:.2f} realizado com sucesso.")

