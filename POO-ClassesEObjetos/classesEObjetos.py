# Criando a Classe Casa():
class Casa():
    imobiliaria = "CTRL Imóveis"

    def __init__(self, rua, bairro, CEP):
        self.rua = rua
        self.bairro = bairro
        self.CEP = CEP

    def getImobiliaria(self):
        return self.imobiliatria
    
    def getRua(self):
        return self.rua
    
    def getBairro(self):
        return self.bairro
    
    def getCEP(self):
        return self.Cep
    
    def setImobiliaria(self, i):
        self.imobiliaria = i
    
    def setRua(self, r):
        self.rua = r

    def setBairro(self, b):
        self.bairro = b

    def setCEP(self, c):
        self.CEP = c

    def enderecoCompleto(self):
        return "Endereço Completo: " + self.rua + ", " + self.bairro + " - CEP: " + self.CEP
    

#Criando  Objeto casa1:    
casa1 = Casa(rua = "Blue Street", bairro="Good Neighborhood", CEP="1234")
casa2 = Casa(rua = "Black Street", bairro="Bad Neighborhood", CEP="4321")
casa3 = Casa("Green Street", "Medium Neigborhood", "54612")

#Acessando atributo de um objeto:
print(casa1.CEP)

print(casa1.enderecoCompleto())

# Criando a classe Cachorro:

class Cachorro:
     def __init__(self, nome, raca):
         self.nome = nome
         self.raca = raca

     def latir(self):
        print(F"{self.nome} está Latindo!")

#Criando objeto CAchorro:
meuCachorro = Cachorro("Bartolomeu", "Salsicha")

novoCachorro = Cachorro("Lupita", "Golden")

cachorro3 = Cachorro("Bob", "Buldog")

#cachorro3.latir()

#novoCachorro.latir()

#meuCachorro.latir()


