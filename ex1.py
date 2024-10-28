def calcular_idade(idade_em_dias):
  anos = idade_em_dias // 365
  dias_rest = idade_em_dias % 365
  meses = dias_rest // 30
  dias = dias_rest % 30

  return anos, meses, dias

if __name__ == "__main__":
  idade_dias = int(input("Digite a idade em dias: "))
  anos, meses, dias = calcular_idade(idade_dias)
  print(f"A idade é de {anos} anos, {meses} meses e {dias} dias.")