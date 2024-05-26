#Curso  Básico de Python
#Nome do Desenvolvedor: Dailton Fernandes
#Versão: 1.0
#Exercício de Lógica de Programação: Linguagem de Programação Python
#Exercício: Números divisíveis por 4 menores que 200


contador = 1


for numero in list(range(1, 200)):
    
    if numero % 4 == 0:
       
        print(numero,"é um número divisível por 4.")
        contador += 1
