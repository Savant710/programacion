# transformar temperatura de centigrados a farenheit y viceversa
temp = float(input("Ingrese la temperatura a convertir: "))
print(temp)
tipo = (input("Que tipo de temperatura es ? (C) Centigrados, (F) Farenheit, (K) kelvin:  ")).lower()
if tipo == "c":
    print(temp ,"C")
    convert = input("Quiere convertir a (F)Farenheit o a (K) kelvin: ").lower()
    if convert == "f":
        tempf = (temp * 1.8) + 32
        print(tempf , "F")
    else:
        tempk = (temp +273)
        print(tempk ,"K")
elif tipo == "f" :
    print(temp , "F")
    convert = input("Quiere convertir a (C)Centigrados o a (K) kelvin: ").lower()
    if convert == "c":
        tempc = (temp -32)* 5/9
        print(tempc , "C")
    else:
         tempk = (temp-32 )* 5/9 +273
         print(tempk , "K")
elif tipo == "k":
    print(temp , "K")
    convert = input("Quiere convertir a (C)Centigrados o a (F) Farenheit: ").lower()
    if convert =="c":
        tempc = (temp - 273)
        print(tempc ,"C")
    else:
         tempf = ((temp-273 )*1.8)+32
         print(tempf , "K")
else:
    print("Valor Ingresado Incorrecto")