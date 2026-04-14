#RETROALIMENTACIÓN GA2
#Análisis de Sistemas
#Leslie Pamela Velásquez Tzarax (29)

#6. Escribir un programa que lea un entero positivo n, introducido por el usuario
#y después muestre en pantalla la usma de todos los enteros desde 1 hasta n.
#La suma de los n primeros enteros positivios puede ser calculada de la siguiente forma:
#Suma = (n(n+1))/2

n = int(input("Introduce un número entero: "))
suma = ((n * (n + 1)) / 2)
print("La suma de los primeros números enteros desde 1 hasta " + str(n) + " es " + str(suma))