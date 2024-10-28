def inverter_palavras(frase):
    palavras = frase.split()
    palavras_invertidas = [palavra[::-1] for palavra in palavras]
    nova_frase = ' '.join(palavras_invertidas)
    return nova_frase


frase = input("\nEscreva uma frase qualquer:\n")
print(inverter_palavras(frase))  
