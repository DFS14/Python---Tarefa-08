#Curso  Básico de Python
#Nome do Desenvolvedor: Dailton Fernandes
#Versão: 1.0
#Exercício de Lógica de Programação: Linguagem de Programação Python
#Exercício: Calcular a soma dos números pares de 1 a 500


soma = 0

for numero in list(range(1, 501)):
  
    if numero % 2 == 0:
   
        soma += numero

print("A soma dos números pares de 1 até 500 é:", soma)

