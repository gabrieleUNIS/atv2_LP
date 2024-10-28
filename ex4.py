import math

print("\nÉ primo?\n")

def e_primo(n):
    
    if n < 2:
        return False
   
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

numero = int(input("Digite um número inteiro qualquer: "))

if e_primo(numero):
    print(f"Verdadeiro\n{numero} é um número primo.\n")
else:
    print(f"Falso\n{numero} não é um número primo.\n")