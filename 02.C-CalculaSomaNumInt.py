#Curso  Básico de Python
#Nome do Desenvolvedor: Dailton Fernandes
#Versão: 1.0
#Exercício de Lógica de Programação: Linguagem de Programação Python
#Exercício: Calcular a soma dos primeiros 100 números inteiros



soma = 0

for numero in list(range(1, 101)):
   
    soma += numero

print("A soma dos primeiros 100 números inteiros é:", soma)
