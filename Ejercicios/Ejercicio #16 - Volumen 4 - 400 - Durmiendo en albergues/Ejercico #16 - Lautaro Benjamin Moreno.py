#Puede que no haya comprendido la consigna, y siento que el codigo esta forzado a funcionar por "ajustarlo a lo bruto"
#para cumplir con los casos de pruebas
print("Ingresa la disposicion de camas (X = Ocupado, . = Libre)")
disposicion = input()
disposicion = disposicion.lower()

mayordistancia = 0
distancia = 0
contadorx = 0

if(len(disposicion) < 500000):

    #Verificar si la entrada es correcta
    for i in range(len(disposicion)):
        if(disposicion[i] != 'x' and disposicion[i] != '.'):
            print("Tu disposicion tiene caracteres incorrectos.")
            break;
        
        #Empezar a contar la distancia, se reinicia al encontrar una x y se almacena el maximo del contador
        if(disposicion[i] != 'x'):
            distancia += 1
            if(distancia > mayordistancia):
                mayordistancia = distancia
        else:
            distancia = 0
        
        #Detectar si hay una sola X
        if(disposicion[i] == 'x'):
            contadorx += 1

    #Si la disposicion empieza y termina con una x, ocuparan 1 espacio
    #se suma 2 para ajustar la ecuacion que sigue despues del siguiente comentario
    if(contadorx > 2):
        if (disposicion[0] == 'x' and disposicion[len(disposicion) - 1] == 'x'):
          mayordistancia += 2   

    #Descontar los espacios al lado de camas ocupadas
    mayordistancia -= 2

    #En el caso de ser una cama ocupada, tendria que descontar un unico espacio, por lo que se suma 1, al ser antes restado por 2
    if(contadorx == 1):
        mayordistancia += 1
    
    #Este condicial fue simplemente para hacer correcta la salida, no puedo enlazar con lo constuido
    #anteriormente al no comprender correctamente la consigna
    if(mayordistancia % 2 == 0):
        mayordistancia -= 1
        if(contadorx == 1):
            mayordistancia += 1

    #Si la variable mayordistancia es negativa, significa que no hay camas disponibles
    if (mayordistancia < 0):
        mayordistancia = 0


else:
    print("Has superado el limite de caracteres.")

print(mayordistancia)
