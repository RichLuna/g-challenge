#Abrimos el documento con el numero e. Puedes ingorar completamente esta parte
def open_e():
	e_file = open("euler.txt")
	e = e_file.read()
	return e

#########################################################################
#Start challenge here
########################################################################

"""
Encuentra la primer cifra de 10 dígitos que sea un numero primo 
dentro de los digitos de el número de Euler. 

Los números primos son aquellos que solo pueden dividirse entre 1 y 
ellos mismos.

Ejemplo:

El número e es:
2.718281828459045235360287471352662497757...

La primer cifra de 10 dígitos es 7182818284 y no es primo.
La segunda cifra es 1828182845 y tampoco es primo

etc


La función "open_e()" regresa el número e con aproximadamente un millón
de dígitos de precisión.


PRO TIPS	

1. Primero resuelve el probema. Después optimiza, pero solo si es necesario
2. Las cadenas son iterables como listas. Eso quiere decir que puedes iterar sobre ellas con un for
3. Igualmente puedes usar slices con cadenas
4. Divide y vencerás. Si separas tareas en funciones puede que el ejercicio sea mas claro
5. Python está muy bien documentado. Si lo necesitas consulta: https://docs.python.org/3/library/string.html
6. La repsuesta es 7427466391. Lo importante es el código, no la repsuesta.


"""

#Obtenemos el número e
e = open_e()

def isPrime(number):
    for i in range(2, number):
        if (number % i) == 0:
            return False
    return True

def findPrimeNumber (eulerNumberList):
    indexStart = 2
    indexFinal = 12    
    
    for element in eulerNumberList[2:]:
        list = eulerNumberList[indexStart:indexFinal]
        sum = 0
        for x in list:
            sum += int(x)
    
        checkPrime = isPrime(sum)
                
        if(checkPrime):
            return list
        
        indexStart+=1
        indexFinal+=1
    
    return "Not Found"
    


output = findPrimeNumber(e)
print(output)

