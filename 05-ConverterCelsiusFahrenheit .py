#Curso  Básico de Python
#Nome do Desenvolvedor: Dailton Fernandes
#Versão: 1.0
#Exercício de Lógica de Programação: Linguagem de Programação Python
#Exercício: Converter graus Celsius em Fahrenheit, de 10 em 10 graus,


for celsius in list(range(10, 101, 10)):
 
    fahrenheit = (9 * celsius + 160) / 5
      
    print(celsius, "°C =", fahrenheit, "°F")