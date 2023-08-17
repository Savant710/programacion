#clases 
# es un contenedor o modelo bajo el cual se va a trabajar
class Auto:
    def __init__(self, marca, modelo, placa):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        print(f'Me compre un nuevo auto. La marca es: {marca}, el modelo es: {modelo}, El numero de placa es: {placa}')
    def escolor(self, color):
        self.color = color
        print(f'El color del carro es:{color}')



        
mi_auto = Auto('wolsvaguen','golf','ABB-777')
mi_auto.escolor('Rojo')
print(mi_auto.escolor)


