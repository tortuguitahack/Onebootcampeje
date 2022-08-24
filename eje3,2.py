#indice de masa corporal
def imc(estatura, peso):

    return peso / estatura**2


peso = float(input("¿Escriba su peso en kilogramos")) 
estatura = float(input("¿Escriba su estatura en metros"))

indice = imc(estatura, peso)


print("Tu indice de masa corporalm es: {}".format(indice))

