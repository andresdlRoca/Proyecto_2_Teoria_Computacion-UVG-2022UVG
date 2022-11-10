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

#cero(f,x)
cero = lambda f: lambda x: x

#uno(f,x)

#dos(f,x)

#tres(f,x)

#sucesor(n,f,x)
sucesor = lambda n: lambda f: lambda x: f(n(f)(x))

#suma(a,b,f,x)
suma = lambda a: lambda b: lambda f: lambda x: a(f)(b(f)(x))

#multiplicacion(a,b,f,x)
multiplicacion = lambda a: lambda b: lambda f: lambda x: a(b(f))(x)

#potencia(a,b,f,x)
potencia = lambda a: lambda b: b(a)

#Alpha
alpha = lambda x: x+1

#Beta
beta = lambda x: 2*x