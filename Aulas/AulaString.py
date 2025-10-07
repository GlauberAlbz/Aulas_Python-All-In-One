frase = "Infoco Consultoria e Treinamentos"

print(50*"-") # Contando caracteres em strings

print(len(frase)) # len -> Conta a quantidade de caracteres da frase(espaços contam)

print(frase[7: 18: 2]) # Seleciona a área que vai imprimir [x: y: z] x -> inicio da contagem, y - final da contagem, z - espaços entre a contagem
print(frase[:5]) # Inicia a contagem desde o inicio até o 5
print(frase[21:]) # Inicia a contagem a partir do 21 caractere em diante

print(50*"-") # Consultando e procurando itens em Strings

print(frase.count("o")) # Conta a quatidade de aparições do item desejado
print(frase.find("Tre")) # Localiza o item desejado, caso não encontre, valor = -1
print("Etec" in frase) # Pergunta se existe a palavra Etec na var frase

print(50*"-") # Transformando Strings

print(frase.replace("Infoco", "Lindolfo")) # Mudar Infoco para Lindolfo

print(frase.upper()) # Deixa tudo maiusculo
print(frase.lower()) # Deixa tudo minusculo
print(frase.capitalize()) # Deixa a primeira letra da frase maiuscula
print(frase.title()) # Deixa a primeira letra das palavras maiusculas

nome = "    Lindolfo J unior   "
nomeOK = nome.strip() # Tira os espaços da direita e da esquerda

print(len(nome))
print(nome)
print(nome.strip())
print(len(nomeOK))

print(nome.rstrip()) # Tira os espaços da direita
print(nome.lstrip()) # Tira os espações da esquerda

print(50*"-") # Divisão de strings

frase2 = frase.split()
print(frase2)

divido = frase.split()

print(divido[3])
print(divido[3][2])

frase3 = "-".join(frase2)
print(frase3)



