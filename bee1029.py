# -*- coding: utf-8 -*-

def fibonacci(n):
	resposta = [0, 1]
	chamadas = [0, 0]
	for i in range(2, n + 1):
		resposta.append(resposta[i - 1] + resposta[i - 2])
		chamadas.append(chamadas[i - 1] + chamadas[i - 2] + 2)
	return chamadas[n], resposta[n]

j = int(input())
for i in range(j):
	n = int(input())
	x, y = fibonacci(n)
	print ("fib(%i) = %i calls = %i") %(n, x, y)