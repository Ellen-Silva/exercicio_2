km = int(input("Quantos KM foram percorridos?"))
dias = int(input("Quantos dias foram percorridos?"))

preco = 60 * dias + 0.15 * km
print(f"KM = {km}. Dias: {dias}")
print(f"Valor a ser pago: {preco}")