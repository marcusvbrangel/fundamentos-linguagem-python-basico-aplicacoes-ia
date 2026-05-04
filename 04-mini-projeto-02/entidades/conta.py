
from abc import ABC, abstractmethod
from datetime import datetime
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

        self._numero = numero
        self._saldo = 0.0
        self._cliente = cliente
        self._transacoes = []
        Conta._total_contas += 1


    # getter para o saldo, permitindo acesso controlado
    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero
    
    @classmethod
    def get_total_contas(cls):
        return cls._total_contas
    
    def depositar(self, valor: float):

        if valor > 0:
            self._saldo += valor
            self._transacoes.append((datetime.now(), f"Depósito de R${valor:.2f}"))
            print(f"Depósito de R${valor:.2f} realizado com sucesso")
        else:
            print("Valor de depósito inválido")            

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



#-------------------------------------------------------------
# ---------- conta corrente ----------------------------------

class ContaCorrente(Conta):

    def __init__(self, numero: int, cliente: Cliente, limite: float = 500.00):

        super().__init__(numero, cliente)
        self.limite = limite

    def sacar(self, valor: float):

        if valor <= 0:
            print("Valor de saque inválido")
            return
        
        saldo_disponivel = self._saldo + self.limite

        if valor > saldo_disponivel:
            raise SaldoInsuficienteError(saldo_disponivel, valor, "Saldo e limite insuficientes.")

        self._saldo -= valor

        self._transacoes.append((datetime.now(), f"Saque de R${valor:.2f}"))
        print(f"Saque de R${valor:.2f} realizado com sucesso.")



#-------------------------------------------------------------
# ---------- conta poupanca ----------------------------------

class ContaPoupanca(Conta):

    def __init__(self, numero: int, cliente: Cliente):

        super().__init__(numero, cliente)
    
    def sacar(self, valor: float):

        if valor <= 0:
            print("Valor de saque inválido")
            return
        
        if valor > self._saldo:
            raise SaldoInsuficienteError(self.saldo, valor)

        self._saldo -= valor

        self._transacoes.append((datetime.now(), f"Saque de R${valor:.2f}"))
        print(f"Saque de R${valor:.2f} realizado com sucesso.")




