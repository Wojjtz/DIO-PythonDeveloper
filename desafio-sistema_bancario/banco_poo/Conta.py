import Historico
import Transacao

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001" 
        self._cliente = cliente
        self._historico = Historico.Historico()

    @classmethod
    def criar_nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self._saldo
        if valor > saldo:
            print("\nOperação falhou! Você não tem saldo suficiente.")

        elif valor > 0:
            self._saldo -= valor
            print(f"\nSaque realizado com sucesso! \nValor sacado: R${valor:.2f} \nSaldo atual: R${self._saldo:.2f}")
            return True

        else:
            print("\nOperação falhou! O valor informado é inválido.")

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"\nDepósito realizado com sucesso! \nValor depositado: R${valor:.2f} \nSaldo atual: R${self._saldo:.2f}")
        else:
            print("\nOperação falhou! O valor informado é inválido.")
            return False
        
        return True

class ContaCorrente(Conta):
    def __init__ (self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Transacao.Saque.__name__]
        )

        if valor > self.limite:
            print("\noperação falhou! O valor de saque excede o limite.")

        elif numero_saques >= self.limite_saques:
            print("\nOperação falhou! Número máximo de saques excedido.")

        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"""\
            Agência:\t{self._agencia}
            C/C:\t\t{self._numero}
            Titular:\t{self._cliente.nome}
        """