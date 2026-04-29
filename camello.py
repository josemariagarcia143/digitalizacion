#Aquí debes introducir el código Python para recrear el Juego del Camello que encontarás en el Taller 4 de Programarcadegames

import random

print('EL CAMELLO\nUn videojuego de gestión de recursos\n\nTu objetivo es escapar de un desierto mientras unos nativos te persiguen por haber robado un camello suyo.\nDebes procurar que no te atrapen, no morir de deshidratación bebiendo de tu cantimplora (que tampoco es infinita) o fallecer por cansancio, al fin y al cabo estás en un desierto donde el sol pega fuerte.\nUna serie de eventos aleatorios podrían darte un golpe de suerte o todo lo contrario, nunca bajes la guardia.\nGuarda objetos en tu mochila de tres espacios y procura hacer uso de ellos estratégicamente.')

#Cosas importantes

game = True

turno = True

#Variables

hora = 0
nat = 50
fin = 150
sed = 5
can = 5
agu = 200
moc = 0

obj1 = 0
obj2 = 0
obj3 = 0

while game == True:

    #Arreglos de números negativos a cero

    if agu < 0:
        agu = 0
    if nat < 0:
        nat = 0
    if sed < 0:
        sed = 0
    if fin < 0:
        fin = 0
    if can < 0:
        can = 0

    while turno == True and nat > 0 and sed < 100 and fin > 0 and can < 100:

        #Dificultades dinámicas

        if hora > 14:
            nat = nat - random.randrange(15, 26)
        elif hora > 7:
            nat = nat - random.randrange(10, 21)
        else:
            nat = nat - random.randrange(5, 16)

        #Hora

        hora = hora + 1

        print('\nHORA',hora)
        print('\nLos nativos se encuentran a',nat,'km de ti.\nEl final del desierto está a',fin,'km de ti.\nTienes',sed,'de 100 de sed.\nTu cansancio es de',can,'de 100.\nTe quedan',agu,'centilitros de agua en la cantimplora.')

        if moc == 0:
            print('No llevas objetos en tu mochila. Son tres espacios libres.')
        elif moc == 1:
            print('Solamente tienes',obj1,'en tu mochila. Son dos espacios libres.')
        elif moc == 2:
            print('Tienes',obj1,'y',obj2,'en tu mochila. Es un espacio libre.')
        else:
            print('Tienes',obj1,'además de',obj2,'y',obj3,'en tu mochila. No quedan espacios libres.')
    
        print('\n1. Beber de la cantimplora.\n2. Caminar hacia adelante.\n3. Detenerse y descansar.\n4. Utilizar un objeto.')
        opc = input('Elige: ')

        #Fin del turno
                       
        turno = False

        #Beber de tu cantimplora

        if opc == '1':
            if agu == 0:
                print('\nNo tienes agua disponible; has perdido tu turno.')
            else:
                print('\nTe quedan',agu,'centilitros de agua en tu cantimplora.')
                beber = int(input('Escribe cuántos quieres beber: '))
                if beber > agu:
                    print('\nNo tienes tanta agua; has perdido tu turno.')
                else:
                    agu = agu - beber
                if sed == 0:
                    print('\nHas bebido',beber,'centilitros de tu cantimplora, ahora hay',agu,'en ella.\nTu sed no ha bajado de',sed,'de 100.\nTu cansancio se mantiene como estaba antes.')
                else:
                    sed = sed - round(beber/2)
                    if sed < 0:
                        sed = 0
                    print('\nHas bebido',beber,'centilitros de tu cantimplora, ahora hay',agu,'en ella.\nTu sed ha bajado a',sed,'de 100.\nTu cansancio se mantiene como estaba antes.')

        #Caminar hacia adelante
        
        elif opc == '2':
            caminar = int(input('Escribe cuántos kilómetros de 40 quieres caminar: ')
        
        turno = True

