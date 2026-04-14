#RETROALIMENTACIÓN GA2
#Análisis de Sistemas
#Leslie Pamela Velásquez Tzarax (29)

#11.Una panadería vende filas de pan a Q. 3.49 cada una. El pan que no es el día
#tiene un descuento del 60%. Escribe un programa que comience leyendo el
#número de filas vendidas que no son del día. Después tu programa debe
#mostrar el precio habitual de una fila de pan, el descuento que se le hace por
#no ser fresca y el coste final total.

barreras = int(input("Introduce el número de filas vendidas que no son frescas: "))
precio = 3.49
descuento = 0.6
coste = barreras * precio * (1 - descuento)
print("El coste de una fila fresca es: " + str(precio) + "Q")
print("EL descuento sobre una fila no fresca es: " + str(descuento * 100) + "%" )
print("El coste final a pagar es: " + str(round(coste, 2)) + "Q")