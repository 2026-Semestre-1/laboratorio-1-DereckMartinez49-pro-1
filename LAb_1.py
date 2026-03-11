
#Nombre: ContarDigitos(num, digito)
#Entrada: num, digito
#Salida: la cantidad de digitos
#Restricciones:Debe ser positivo mayor igual a cero

def contadorDigitos(num, digito):
     if not(isinstance(num, int)):
         return "Error: num debe ser entero"
     elif not (isinstance(digito, int)):
         return "Error: digito debe ser entero"
     elif not 0 <= digito < 10:
         return "Error: digito debe ser mayor igual cero y menor que diez"
     else:
         return contadorDigitos_aux(num, digito)
       
def contadorDigitos_aux(num, digito):
        i = 0
        
        if digito == i:
            return i

        else:
            while num!= 0:
                u = num % 10
                if u == abs (digito):
                 i += 1
                num = num // 10

            return i


"""
Nombre: calculadora(operacion, op1, op2)
#Entrada: operacion, op1, op2
#Salida: suma. resta, multiplicacion, division 
#Restricciones:op1 y 2, deben ser enteros

"""


def calculadora(operacion, op1, op2):
    if not(isinstance(op1, int)):
         return "Error: op1 debe ser entero"
        
    elif not (isinstance(op2, int)):
         return "Error: op2 debe ser entero"
        
    elif 0 < operacion >= 5:
         return "Error: operacion debe ser mayor a cero y menor igual que cuatro"
        
    else:
         return calculadora_aux(operacion, op1, op2)
def calculadora_aux(operacion, op1, op2):
    if (operacion == 1):
        r = (op1 + op2) 
        return r
    elif (operacion == 2):
        r = (op1 - op2) 
        return r
    elif (operacion == 3):
        r = (op1 * op2) 
        return r
    elif (operacion == 4):
        r = (op1 / op2)
        if r == 0:
            return "Error: No es posible la division entre 0"
        
        return r


"""
#Nombre: sumatoria_V2
#Entrada: (inicio, fin, distancia, excepcion)
#Salida: Sumatoria
#Restricciones:Todos parámetros deben ser de tipo entero,
                Los párametros distancia y excepcion debe ser menor a 10 y mayor a 0.
                Los valores de inicio y fin deben ser positivos
                Si la distancia es un número negativo, el valor de fin debe ser menor a inicio
                Si la distancia es un número positivo, el valor de fin debe ser mayor a inicio
                Si excepcion es igual a cero, se debe ignorar este valor, lo contrario, todo número dentro de la secuencia entre inicio y ** final** sea divisible por esta excepcion debe omitirse en la suma

"""

def sumatoria_V2(inicio, fin, distancia, excepcion):
    if not(isinstance(inicio, int)):
         return "Error: inicio debe ser entero"
    elif not inicio > 0:
        return "Error: inicio debe ser positivo"
    
    elif not (isinstance(fin, int)):
         return "Error: fin debe ser entero"

    elif not fin > 0:
        return "Error: fin debe ser positivo"
        
    elif not (isinstance(distancia, int)):
         return "Error: distancia debe ser entero"
    elif not 0 > distancia < 10:
        return "Error: distancia  debe ser menor a diez y mayor a cero"
    

    elif not (isinstance(excepcion, int)):
         return "Error: excepcion debe ser entero"

    elif not 0 > excepcion < 10:
        return "Error: excepcion  debe ser menor a diez y mayor a cero"
