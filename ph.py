ph = int(input('Escribe el Ph: '))
if ph <= 4:
    print('Muy ácido.')
elif ph > 4 and ph < 7:
    print('Poco ácido.')
elif ph == 7:
    print('Neutro.')    
elif ph > 7 and ph <= 10:
    print('Poco alcalino.')
else:
    print('Muy alcalino.')
        
