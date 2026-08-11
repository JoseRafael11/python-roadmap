edad=int(input("cual es su edad"))
boleto=input("tiene boleto?")
representante=int(input("edad del representante?"))
if edad>=18 and boleto=="si" or edad<18 and representante>=18:
    print("si tiene acceso")
else:
    print("no tiene acceso")    