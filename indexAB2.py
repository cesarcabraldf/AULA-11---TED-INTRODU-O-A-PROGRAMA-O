import random

A = [[random.randint(1, 100) for _ in range(10)] for _ in range(10)]


soma_total = sum(sum(linha) for linha in A)


print("Matriz A (10x10):")
for linha in A:
    print(linha)

print("\nSoma de todos os valores da matriz:", soma_total)

# Letra B - 2º Questão - TED 11

import random


A = [[random.randint(1, 100) for _ in range(10)] for _ in range(10)]


B = [[elemento * 3 for elemento in linha] for linha in A]


print("Matriz A (10x10):")
for linha in A:
    print(linha)

print("\nMatriz B (10x10), com elementos de A multiplicados por 3:")
for linha in B:
    print(linha)
