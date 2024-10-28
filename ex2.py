import math

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

if a < b + c and b < a + c and c < a + b:
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(f"Os valores formam um triângulo com área: {area:.2f}")

else:
    print(f"Os valores {a}, {b} e {c} não formam um triângulo.")