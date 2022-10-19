#Gasto de combustível

tempo = int(input())
vm = int(input())
consumo = 12
dist = tempo * vm

litros = dist / consumo

print("{:.3f}".format(litros))