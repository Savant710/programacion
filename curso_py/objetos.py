#class nos permite definir el entorno
#respecto a la cula se van a constuir objetos

class Panaderia:
#init  especifica las acciones en la creacion de un objeto
#self se utiliza para hacer referencia al propio objeto
#en la expresion self.panes diferenciamos ambos valores
    def __init__ (self, panes, pastitas):
        self.panes = panes
        self.pastas= pastitas
        print('En la tienda hay', self.panes, "panes y", self.pastas, 'pastas aunque estas no se venden')
    def vender(self):
        if self.panes > 0:
            print ('Vendido un pan')
            self.panes -= 1
        else:
            print('Lo sentimos no quedan panes para vender')
    def coce(self, piezas):
        self.panes += piezas
        print('Quedan', self.panes, 'panes')
panaderia1 = Panaderia(3,4)
panaderia2 = Panaderia(1,2)

panaderia2.vender()
panaderia2.vender()

panaderia2.coce(7)
panaderia2.vender()


