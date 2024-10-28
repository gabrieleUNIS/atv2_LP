num_1 = int(input("Digite o 1º numero: "))
num_2 = int(input("Digite o 2º numero: "))
num_3 = int(input("Digite o 3º numero: "))

menor = num_1
if num_2 < num_1 and num_2 < num_3:
    menor = num_2
if num_3 < num_1 and num_3 <= num_2:
    menor = num_3


print(f"O menor número é: {menor}")
