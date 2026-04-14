#RETROALIMENTACIÓN GA2
#Análisis de Sistemas
#Leslie Pamela Velásquez Tzarax (29)

#10. Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4%
#de interés al año. Estos ahorros debido a intereses, que no se cobran hasta
#finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir
#un programa que comience leyendo la cantidad de dinero depositada en la
#cuenta de ahorros, introducida por el usuario. Después el programa debe
#calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y
#tercer años. Redondear cada cantidad a dos decimales.

inversion = float(input("Introduce la inversión inicial: ")) #Guardamos como float la inversión inicial.
interes = 0.04 #Guardamos el valor dle interés.
balance1 = inversion * (1 + interes) #Hacemos el cálculo del primer balance.
print("Balance tras el primero año: " + str(round(balance1, 2))) #Imprimos el resultado del primir balance redondeándolo.
balance2 = balance1 * (1 + interes) #Hacemos elcálculo del segundo balance.
print("Balance tras el segundo año: " + str(round(balance2, 2))) #Imprimimos el resultado del segundo balanca redondeándolo.
balance3 = balance2 * (1 + interes) #Hacemos el cálculo del tercer balance.
print("Balance tras el tercer año: " + str(round(balance3, 2))) #Imprimimos el resultado del tercer balance, redondeándolo.
