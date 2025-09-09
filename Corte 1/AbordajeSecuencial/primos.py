#Este ejercicio es para subior una decima en el corte

while True:
    valor = input("Ingrese un valor")
    
    try:
        valor = int(valor)
    except ValueError:
        print ("por favor ingrese el numero correcto")
    for i in range(1, valor + 1):
        conta = 0
        for n in range(1, i + 1):
            residue = i%n
            if residue == 0:
                conta = conta + 1
        
    if conta == 2:
            print(f'{i} es un primo')
    else:
            print(f'{i} NO es un primo')
    


   

    
    