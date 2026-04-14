#RETROALIMENTACIÓN GA2
#Análisis de Sistemas
#Leslie Pamela Velásquez Tzarax (29)

#5. Escribe un programa que pregunte al usuario por el número de horas
#trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

horas = float(input("Introduce tus horas de trabajo: ")) #Guardamos como float las horas trabajadas ingresadas.
coste = float(input("Introduce lo que cobras por hora: ")) #Guardamos como float los costos por hora que ingresa el usuario.
paga = horas * coste #Guardamos en la variable el resultado total de la paga.
print("Tu paga es: ", paga) #Imprimimos el total de pago.