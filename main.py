######################################
#
# Teoria de la computacion
# Grupo 9:
# Yong Park
# Jun Woo Lee
# Andres de la Roca
#
# Proyecto 2
#
######################################

# Gramaticas



# Funciones Lambda
#Referencia 1: https://users.monash.edu/~lloyd/tildeFP/Lambda/Examples/const-int/
#Referencia 2: https://www.glc.us.es/~jalonso/exercitium/numeros-de-church/#:~:text=Los%20n%C3%BAmeros%20naturales%20pueden%20definirse,y%20devuelve%20n%20veces%20f.

#Conversion de funcion lambda/numeros de Church
#Convierte las funciones Lambda a integer que se pueda visualizar en la CLI
#Se suma 1 al argumento x que se le de (funciona como "sucesor")
lambdaToint = lambda n: n(lambda x: x + 1)(0) 

#Funciones de numeros de Church/Lambda: (a-e)
#f = funcion para aplicar
#x = argumento sobre el que se aplica la funcion

#cero(f,x)
cero = lambda f: lambda x: x

#uno(f,x)
uno = lambda f: lambda x: f(x)

#dos(f,x)
dos = lambda f: lambda x: f(f(x))

#tres(f,x)
tres = lambda f: lambda x: f(f(f(x)))

#Funciones de operacion sobre numeros de Church/Lambda (f-h)
# n = Numero de Church sobre el cual se opera
# a & b = Argumentos sobre los cuales se opera

#sucesor(n,f,x)
sucesor = lambda n: lambda f: lambda x: f(n(f)(x))

#suma(a,b,f,x)
suma = lambda a: lambda b: lambda f: lambda x: a(f)(b(f)(x))

#multiplicacion(a,b,f,x)
multiplicacion = lambda a: lambda b: lambda f: lambda x: a(b(f))(x)

#potencia(a,b,f,x)
potencia = lambda a: lambda b: b(a)

#alpha(x+1) = x + 1
alpha = lambda x: suma(x)(uno)

#beta(x) = 2*x
beta = lambda x: multiplicacion(dos)(x)


#Ejemplos de uso
#a.
print("* 2 2:")
print(lambdaToint(multiplicacion(dos)(dos))) # * 2 2
print(" ")
#b.
print("+ + 1 2 sucesor 2 -> + + 1 2 3:")
print(lambdaToint(suma(suma(uno)(dos))(sucesor(dos)))) # + + 1 2 sucesor 2 -> + + 1 2 3
print(" ")
#c. 
print("^ + 1 3 2:")
print(lambdaToint(potencia(suma(uno)(tres))(dos))) # ^ + 1 3 2
print(" ")
#d.
print("+ alpha 2 beta 3")
print(lambdaToint(suma(alpha(dos))(beta(tres)))) # + alpha 2 beta 3