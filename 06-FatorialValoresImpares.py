#Curso  Básico de Python
#Nome do Desenvolvedor: Dailton Fernandes
#Versão: 1.0
#Exercício de Lógica de Programação: Linguagem de Programação Python
#Exercício: Programa imprimi o valor do fatorial dos valores ímpares (1 a 10) 
import math

print(math.factorial(10))  

for numero in list(range(1, 11)):
    if numero % 2 != 0:
        
        f = math.factorial(numero)
        print(numero, "é fatorial de", f, ".")

