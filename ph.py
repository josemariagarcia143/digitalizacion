ph = int(input('Escribe el Ph: '))
if ph <= 4:
    print('Muy ácido.')
elif 4 < ph < 7:
    print('Poco ácido.')
elif ph == 7:
    print('Neutro.')    
elif 7 < ph <= 10:
    print('Poco alcalino.')
else:
    print('Muy alcalino.')
