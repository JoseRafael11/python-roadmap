edad=int(input("edad del cliente"))
tarjeta_frecuente=input("tiene tarjeta de cliente frecuente?")
precio_compra=float(input("precio de la compra?"))
if edad>=18 and tarjeta_frecuente=="si" and precio_compra>=100:
    descuento=0.10
else:
    descuento=0.00
    print("no tiene descuento")
descuento_total=precio_compra*descuento    
precio_total=precio_compra-descuento_total
print("descuento de",descuento_total)
print("precio total es",precio_total)       
