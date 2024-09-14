class Cachorro:
    def __init__ (self, nome, raca, dono, idade):
        self.nome = nome
        self.raca = raca
        self.dono = dono
        self.idade = idade
        self.diag = ""
        self.especie = "Cachorro"

    def latir(self):
        print("LATINDO...")

    def getNome(self):
        return self.nome
    
    def setNome(self, nome):
        self.nome = nome

    def getRaca(self):
        return self.raca
    
    def setRaca(self, raca):
        self.raca = raca

    def getDono(self):
        return self.dono
    
    def setDono(self, dono):
        self.dono = dono

    def getIdade(self):
        return self.idade
    
    def setIdade(self, idade):
        self.idade = idade

    def getEspecie(self):
        return self.especie
    
    def getDiag(self):
        return self.diag
    
    def setDiag(self, diag):
        self.diag = diag
    
     
class Gato:
    def __init__ (self, nome, cor, dono, idade):
        self.nome = nome
        self.cor = cor
        self.dono = dono
        self.idade = idade
        self.diag = ""
        self.especie = "Gato"

    def miar(self):
        print("MIANDOO...")

    def getNome(self):
        return self.nome
    
    def setNome(self, nome):
        self.nome = nome

    def getCor(self):
        return self.cor
    
    def setCor(self, cor):
        self.cor = cor

    def getDono(self):
        return self.dono
    
    def setDono(self, dono):
        self.dono = dono

    def getIdade(self):
        return self.idade
    
    def setIdade(self, idade):
        self.idade = idade

    def getEspecie(self):
        return self.especie
    
    def getDiag(self):
        return self.diag
    
    def setDiag(self, diag):
        self.diag = diag