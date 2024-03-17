## Primeira questão:
numeros = [10, 5, 25, 15, 20, 30, 5]
maior_numero = max(numeros)
print("O maior número na lista é:", maior_numero)

## Segunda questão:
nomes = ["Ana", "Elizabeth", "Maria", "Pedro", "Rayssa"]
total_nomes = len(nomes)
print("Quantidade de nomes na lista é:", total_nomes)

## Terceira questão:
numeros = [10, 5, 20, 15, 25]
soma = sum(numeros)
print("A soma de todos os números da lista é:", soma)

## Quarta questão:
numeros = [10, 5, 20, 15, 25]
media = sum(numeros) / len(numeros)
print("A média dos valores da lista é: ", media)

## Quinta questão:
palavras = ["Abacaxi", "Amor", "Arvore", "Sofrimento", "Solidão"]
contador_A = sum(1 for palavra in palavras if palavra.startswith('A'))
print("A quantidade de palavras que começam com a letra 'A':", contador_A)

## Sexta questão:
palavras = ["gato", "cachorro", "elefante", "hipopotamo"]
mais_longa = max(palavras, key=len)
print("A palavra mais longa da lista é:", mais_longa)

## Sétima questão:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [n for n in numeros if n % 2 == 0]
print("Números pares da lista:",  pares)

## Oitava questão:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
impares = [n for n in numeros if n % 2 != 0]
print("Números impares da lista:", impares)

## Nona questão:
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

numeros_comuns = [numero for numero in lista1 if numero in lista2]
print("Números presentes em ambas as listas:", numeros_comuns)

## Décima questão:
numeros = [1, 2, 3, 4, 5, 6, 6, 7, 8, 8, 9, 9, 9]
numeros_sem_repeticao = list(set(numeros))
print("Lista sem repetição:", numeros_sem_repeticao)
