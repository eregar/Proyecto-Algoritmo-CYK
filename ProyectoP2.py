matriz=[]
cadena=""

class Generador():

    def __init__(self, nombre):
        super(Generador, self).__init__()
        self.nombre= nombre
        self.generadores = [] #array de arrays
        self.terminales = []

    def __str__(self):
        x=[]
        y=[]
        for i in range(len(self.generadores)):
            x.append([])
            for j in range(2):
                x[i].append(self.generadores[i][j].nombre)
        for i in self.terminales:
            y.append(i.nombre)
        return "Nombre %s\ngeneradores %s\nterminales %s\n" %(self.nombre,x,y)

    def checkGen(self,gen1,gen2):
        if [gen1,gen2] in self.generadores:
            return True
        return False

    def checkTer(self,ter1):
        if ter1 in self.generadores:
            return True
        return False

    def appendToGeneradores(self,gen1,gen2):
        self.generadores.append([gen1,gen2])

    def appendToTerminales(self,ter1):
        self.terminales.append(ter1)



class Terminal(object):

    def __init__(self, nombre):
        super(Terminal, self).__init__()
        self.nombre = nombre
#--------------------------------------------------------------------------
def findTer(argumento):
    for ter in range(len(terminals)):
        if terminals[ter].nombre == argumento:
            #si existe en index ter
            return terminals[ter]
    return
        # no existe
def findGen(argumento):
    for ter in range(len(generators)):
        if generators[ter].nombre == argumento:
            return generators[ter]
    return

def tomarInput(inicial,base):
    for i in base:
        if len(i)==1:
            buscar=findTer(i)
            if buscar:
                inicial.appendToTerminales(buscar)
            else:
                nuevo=Terminal(i)
                inicial.appendToTerminales(nuevo)
                terminals.append(nuevo)
        else:
            buscar1=findGen(i[0])
            buscar2=findGen(i[1])
            if buscar1 and buscar2:
                inicial.appendToGeneradores(buscar1,buscar2)
            elif buscar1 and (not buscar2):
                inicial.appendToGeneradores(buscar1,Generador(i[1]))
            elif (not buscar1) and  buscar2:
                inicial.appendToGeneradores(Generador(i[0]),buscar2)
            else:
                inicial.appendToGeneradores(Generador(i[0]),Generador(i[1]))

print("Bienvenido, porfavor ponga Generadores o terminal separado por espacio")
print("version ALFA 0.0.1 porfavor solo ponga Gramatica en FNdC")
print("Ejemplo: S-> AB CD HI DC BA JJ a b c")
base=input("S -> ")
base=base.split()
principio= Generador("S")
generators=[]
terminals=[]
tomarInput(principio,base)
print(principio)
