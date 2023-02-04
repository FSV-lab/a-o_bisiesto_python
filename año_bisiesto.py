año = 2024 #El año que queremos comprobar
def año_bisiesto():
    
    if año % 4 != 0:
        print("No  es Bisiesto")
    elif año % 4 == 0 and año % 100 != 0:#Divisible 4 y no entre 100 o 400
        print("Es Bisiesto")
    elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0:#Divisible entre 4 y 10 y no entre 400  
        print("No es Bisiesto")
    elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0:#Divisible entre 4 y 100 y 400
        print("Es Bisiesto") 

año_bisiesto()