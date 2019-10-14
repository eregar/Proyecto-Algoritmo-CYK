
class Generador():

    def __init__(self, nombre):
        super(Generador, self).__init__()
        self.nombre= nombre
        self.generadores = [] #array de arrays
        self.terminales = []

    def __str__(self):
        #x=[]
        #y=[]
        #for i in range(len(self.generadores)):
        #    x.append([])
        #    for j in range(2):
        #        x[i].append(self.generadores[i][j].nombre)
        #for i in self.terminales:
        #    y.append(i.nombre)
        #return "Nombre %s\ngeneradores %s\nterminales %s\n" %(self.nombre,x,y)
        return self.nombre

    def checkGen(self,gen1,gen2):
        if [gen1,gen2] in self.generadores:
            return True
        return False

    def checkTer(self,ter1):
        if ter1 in self.terminales:
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

            buscar=findTer(i.lower())
            if buscar:
                inicial.appendToTerminales(buscar)
            else:
                nuevo=Terminal(i.lower())
                inicial.appendToTerminales(nuevo)
                terminals.append(nuevo)
        elif len(i)==2:
            buscar1=findGen(i[0].upper())
            buscar2=findGen(i[1].upper())
            if buscar1 and buscar2:
                inicial.appendToGeneradores(buscar1,buscar2)
            elif buscar1 and (not buscar2):
                nuevo1=Generador(i[1].upper())
                inicial.appendToGeneradores(buscar1,nuevo1)
                generators.append(nuevo1)
            elif (not buscar1) and  buscar2:
                nuevo1=Generador(i[0].upper())
                inicial.appendToGeneradores(nuevo1,buscar2)
                generators.append(nuevo1)
            else:
                if i[0].upper()!=i[1].upper():
                    nuevo1=Generador(i[0].upper())
                    nuevo2=Generador(i[1].upper())
                    generators.append(nuevo1)
                    generators.append(nuevo2)
                    inicial.appendToGeneradores(nuevo1,nuevo2)
                else:
                    nuevo1=Generador(i[0].upper())
                    generators.append(nuevo1)
                    inicial.appendToGeneradores(nuevo1,nuevo1)
        else:
             raise RuntimeError('No se puede tener 3 letras en un espacio')

def addM(menor,mayor,dato):
    if "0" in matriz[mayor][menor]:
        matriz[mayor][menor]=[dato]
    else:
        matriz[mayor][menor].append(dato)
def getM(menor, mayor):
    return matriz[mayor][menor]
def backtrack(menor,mayor,index,nivel,delta):
    print("me iamaron?")
    for x in cadena:
        impresion.append("")
    backtrackR(menor,mayor,index,nivel,delta)
    for x in reversed(impresion):
        print(x)

def backtrackR(menor,mayor,index,nivel,delta):
    gen=getM(menor,mayor)[index]
    res=(" "*(delta)+"|"+"-"*delta+str(gen)+"-"*delta+"|"+" "*(delta+1))
    impresion[nivel]+=res
    if menor==mayor:
        res=(" "*delta*2+cadena[menor]+" "*delta*2+" ")
        impresion[nivel-1]+=res
        counter=nivel-2
        while counter>=0:
            impresion[counter]+=" "*(delta+1)*4
            counter-=1
    else:
        downm=mayor#decrementar
        downp=mayor
        leftm=menor
        leftp=mayor-1#decrementar
        # empieza en mayor mayor
        while leftm<=leftp:
            left=getM(leftm,leftp)
            down=getM(downm,downp)
            for leftside in range(len(left)):
                for downside in range(len(down)):
                    if gen.checkGen(left[leftside],down[downside]):
                        backtrackR(leftm,leftp,leftside,nivel-1,delta//2)
                        backtrackR(downm,downp,downside,nivel-1,delta//2)
                        return
            downm-=1
            leftp-=1

        #como se hizo
        #backtrack()
print("Bienvenido, porfavor ponga Generadores o terminal separado por espacio")
print("version ALFA 0.0.1 porfavor solo ponga Gramatica en FNdC")
print("Ejemplo: S-> AB CD HI DC BA JJ a b c")
matriz=[]
impresion=[""]
principio= Generador("S")
generators=[]
terminals=[]
generators.append(principio)
i=0
while i < len(generators):
    base=input("%s -> " % generators[i].nombre)
    base=base.split()
    tomarInput(generators[i],base)
    i+=1
cadena=input("Cadena a verificar: ")
cadena=cadena.lower()
#hacer media tabla
for i in range(len(cadena)):
    matriz.append([])
    for j in cadena:
        matriz[i].append("0")
for i in range(len(cadena)):
    for j in generators:
        if j.checkTer(findTer(cadena[i])):
            addM(i,i,j)


for distance in range(1,len(cadena)):
    for i in range(len(cadena)-1):
        menor=i
        mayor=i+distance
        if mayor>=len(cadena):
            break
        for c in range(1,distance+1):
            left=getM(menor,mayor-1-distance+c)
            down=getM(menor+c,mayor)
            for leftside in left:
                for downside in down:
                    for j in generators:
                        if j.checkGen(leftside,downside):
                            addM(menor,mayor,j)
for i in matriz:
    for x in i:
        for y in x:
            print(y, end=',')
        print(end=' ')
    print()
resultados=getM(0,len(cadena)-1)
for variable in range(len(resultados)):
    if resultados[variable]!="0":
        if resultados[variable].nombre!="S":
            print("la cadena no pertenece a la gramatica")
        else:
            levels=len(cadena)
            print("llamando backtrack")
            backtrack(0,len(cadena)-1,variable,levels,levels*3)
            print("si pertenece a la gramatica")
            break
    else:
        print("la cadena no pertenece a la gramatica")
        break
