import math
from abc import ABC, abstractmethod

class Operacao(ABC):
    # classe base abstrata que representa qualquer operacao da calculadora, define o executar que toda operacao precisa cumprir
    # a calculadora vai chamar executar sem saber qual subclasse recebeu

    @abstractmethod
    def executar(self):
        pass

    def descricao(self):
        # descricao padrao usada no historico cada subclasse pode sobrescrever
        return self.__class__.__name__

class Soma(Operacao):
    # subclasse que herda de Operacao e usa o metodo executar a sua maneira

    def __init__(self, a, b):
        self._a = a
        self._b = b

    def executar(self):
        return self._a + self._b

    def descricao(self):
        return f"{self._a} + {self._b}"

class Subtracao(Operacao):
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def executar(self):
        return self._a - self._b

    def descricao(self):
        return f"{self._a} - {self._b}"

class Multiplicacao(Operacao):
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def executar(self):
        return self._a * self._b

    def descricao(self):
        return f"{self._a} * {self._b}"

class Divisao(Operacao):
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def executar(self):
        if self._b == 0:
            raise ValueError("Nao e possivel dividir por zero")
        return self._a / self._b

    def descricao(self):
        return f"{self._a} / {self._b}"

class RaizQuadrada(Operacao):
    def __init__(self, n):
        self._n = n

    def executar(self):
        if self._n < 0:
            raise ValueError("Nao e possivel calcular raiz quadrada de numero negativo")
        # usa a funcao da biblioteca
        return math.sqrt(self._n)

    def descricao(self):
        return f"raiz({self._n})"

class Calculadora:
    # classe responsavel por executar operacoes e manter o historico delas
    # o historico fica numa lista privada acessada so pela property abaixo
    def __init__(self):
        self._historico = []

    def executar_operacao(self, operacao):
        resultado = operacao.executar()
        self._historico.append(f"{operacao.descricao()} = {resultado}")
        return resultado

    @property
    def historico(self):
        # devolve uma copia para o chamador nao poder alterar a lista interna
        return list(self._historico)

class MenuCalculadora:

    def __init__(self):
        self._calculadora = Calculadora()

    def ler_numero(self, mensagem):
        # centraliza a leitura de numero pra nao repetir o try em cada opcao
        while True:
            try:
                return float(input(mensagem))
            except ValueError:
                print("Entrada invalida digite um numero")

    def executar_soma(self):
        a = self.ler_numero("Digite o primeiro numero: ")
        b = self.ler_numero("Digite o segundo numero: ")
        self._mostrar_resultado(Soma(a, b))

    def executar_subtracao(self):
        a = self.ler_numero("Digite o primeiro numero: ")
        b = self.ler_numero("Digite o segundo numero: ")
        self._mostrar_resultado(Subtracao(a, b))

    def executar_multiplicacao(self):
        a = self.ler_numero("Digite o primeiro numero: ")
        b = self.ler_numero("Digite o segundo numero: ")
        self._mostrar_resultado(Multiplicacao(a, b))

    def executar_divisao(self):
        a = self.ler_numero("Digite o primeiro numero: ")
        b = self.ler_numero("Digite o segundo numero: ")
        self._mostrar_resultado(Divisao(a, b))

    def executar_raiz(self):
        n = self.ler_numero("Digite o numero: ")
        self._mostrar_resultado(RaizQuadrada(n))

    def _mostrar_resultado(self, operacao):
        # metodo para todas as operacoes, porque todas tem a mesma interface, executar isso evita repetir o mesmo try except cinco vezes
        try:
            resultado = self._calculadora.executar_operacao(operacao)
            print(f"Resultado: {resultado}")
        except ValueError as erro:
            print(f"Erro: {erro}")

    def _mostrar_historico(self):
        historico = self._calculadora.historico
        if not historico:
            print("Nenhuma operacao realizada ainda")
            return
        for item in historico:
            print(item)

    def exibir(self):
        opcoes = {
            "1": self.executar_soma,
            "2": self.executar_subtracao,
            "3": self.executar_multiplicacao,
            "4": self.executar_divisao,
            "5": self.executar_raiz,
            "6": self._mostrar_historico,
        }
        while True:
            print("\n--- Calculadora ---")
            print("1 - Somar")
            print("2 - Subtrair")
            print("3 - Multiplicar")
            print("4 - Dividir")
            print("5 - Raiz quadrada")
            print("6 - Ver historico")
            print("0 - Sair")

            escolha = input("Escolha uma opcao: ")

            if escolha == "0":
                print("Encerrando")
                break

            acao = opcoes.get(escolha)
            if acao is None:
                print("Opcao invalida tente novamente")
                continue
            acao()


menu = MenuCalculadora()
menu.exibir()