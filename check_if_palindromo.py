# Vamos testar se uma palavra é um palíndromo?!

palavra = input("Digite uma palavra: ")

# Inverte a palavra usando a técnica de fatiamento de string
palavra_invertida = palavra[::-1]

if palavra == palavra_invertida:
    print("A palavra", palavra, "é um palíndromo.")
else:
    print("A palavra", palavra, "não é um palíndromo.")
