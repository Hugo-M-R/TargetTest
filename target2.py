# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
def diferenca(n):
    a, b = 0, 1
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b
    return False
n = int(input("Digite algum número: "))
if diferenca(n):
 print("O número {} pertence à sequência".format(n))
else:
 print("O número {} não pertence à sequência".format(n))