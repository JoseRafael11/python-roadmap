nombre=input("cual es su nombre?")
edad=int(input("cual es su edad?"))
precio=float(input("cual es el precio del producto?"))
if edad>=18 and edad<=25:
    descuento=0.10
    
elif edad>=26 and edad<=30:
    descuento=0.20
        
elif edad>=31 and edad<=50:
    descuento=0.30
    
else:
    print("no hay descaunto, su precio es:",precio)

descuento_total=precio*descuento
precio_final=precio-descuento_total    

print("que tal",nombre)
print("su descuento es",descuento_total)
print("su precio total es:",precio_final)        