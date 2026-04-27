#Aquí debes introducir el código Python para recrear el Juego del Camello que encontarás en el Taller 4 de Programarcadegames



print('EL CAMELLO\nUn videojuego de gestión de recursos\n\nTu objetivo es escapar de un desierto mientras unos nativos te persiguen por haber robado un camello suyo.\nDebes procurar que no te atrapen, no morir de deshidratación bebiendo de tu cantimplora (que tampoco es infinita) o fallecer por cansancio, al fin y al cabo estás en un desierto donde el sol pega fuerte.\nUna serie de eventos aleatorios podrían darte un golpe de suerte o todo lo contrario, nunca bajes la guardia.')

nat = 75
fin = 150
sed = 5
can = 5
agu = 200
moc = 0

obj1 = 0
obj2 = 0
obj3 = 0

print('\nDÍA 1\nLos nativos se encuentran a',nat,'km de ti.\nEl final del desierto está a',fin,'km de ti.\nTienes',sed,'de 100 de sed.\nTu cansancio es de',can,'de 100.\nTe quedan',agu,'centilitros de agua en la cantimplora.')

if moc == 0:
    print('No llevas objetos en tu mochila. Son tres espacios libres.')
elif moc == 1:
    print('Solamente tienes',obj1,'en tu mochila. Son dos espacios libres.')
elif moc == 2:
    print('Tienes',obj1,'y',obj2,'en tu mochila. Es un espacio libre.')
else:
    print('Tienes',obj1,'además de',obj2,'y',obj3,'en tu mochila. No quedan espacios libres.')
    
print('\nA. Beber de la cantimplora.\nB. Caminar hacia adelante.\nC. Detenerse y descansar.\nD. Utilizar un objeto.')
