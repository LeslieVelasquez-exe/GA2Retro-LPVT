#RETROALIMENTACIÓN GA2
#Análisis de Sistemas
#Leslie Pamela Velásquez Tzarax (29)

#7. Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),
#calcule el índice de masa corporal y lo almacene en una variable, e imprima
#por pantalla la frase `Tu índice de masa corporal es <imc>` donde `<imc>` es
#el índice de masa corporal calculado redondeado con dos decimales.

peso = input("¿Cuál es su peso en kg?") #Guardamos en una variable el peso ingresado por el usuario.
estatura = input("¿Cuál es tu estatura en metros?") #Guardamos en una variable la estatura ingresada por el usuario.

imc = round(float(peso) / float(estatura) ** 2, 2) #Guardamos en una variable el imc.
#round()  toma dos argumentos: el número que se va a redondear y un valor opcional de ndigits (precisión).
#Por lo que en este caso, lo primero es el resultado de la operaicón que se va a redondear, segudio de ',' que indica
#la cantidad de decimales que vamos a necesitar, en este caso usamos 2, lo que signfiica que solo mostrará dos decimales.
print("Tu índice de masa corporal es: " + str(imc)) #imprimimos el reusltado pasándolo a String.