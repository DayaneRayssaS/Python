# Solicita a nota do usuário
nota = int(input("Digite sua nota: "))
# Categoriza a nota
if nota < 20:
    categoria = "F"
elif nota < 40:
    categoria = "D"
elif nota < 80:
    categoria = "C"
elif nota < 100:
    categoria = "A+"
elif nota == 100:
    categoria = "S"
elif nota < 90:
    categoria = "A"
# Exibe a categoria
print(f"Você está na categoria: {categoria}.")