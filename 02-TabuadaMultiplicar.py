#Curso  Básico de Python
#Nome do Desenvolvedor: Dailton Fernandes
#Versão: 1.0
#Exercício de Lógica de Programação: Linguagem de Programação Python
#Exercício: Tabuada de multiplicar de um número

numero = int(input("Digite um número: "))

for valor in list(range(1, 11)):
   
    print(numero, "x", valor, "=", numero*valor)
