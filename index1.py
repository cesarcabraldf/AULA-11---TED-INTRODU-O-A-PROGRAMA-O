VET = []
for i in range(10):
    num = int(input(f"Digite o {i + 1}º número: "))
    VET.append(num)

posicoes = {}


for index, numero in enumerate(VET):
    if numero in posicoes:
        posicoes[numero].append(index)
    else:
        posicoes[numero] = [index]


repeticoes_encontradas = False
for numero, indices in posicoes.items():
    if len(indices) > 1:
        print(f"O número {numero} está repetido nas posições: {indices}")
        repeticoes_encontradas = True


if not repeticoes_encontradas:
    print("Não existem números repetidos no vetor VET.")
