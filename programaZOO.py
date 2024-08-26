class Animal:
    def __init__(self,nome,idade,barulho,movimento,alimentacao,habitat,vizinhos,horas_alimentacao):
        self.nome = nome
        self.idade = idade
        self.barulho = barulho
        self.movimento = movimento
        self.alimentacao = alimentacao
        self.habitat = habitat
        self.vizinhos = []
        self.horas_alimentacao = horas_alimentacao
    
    def adicionar_vizinho(self,vizinho):
        if len(self.vizinhos) <2:
            self.vizinhos.append(vizinho)
        else:
            print(f"{self.nome} ja tem o numero maximo de vizinhos")

    def fazer_barulho(self):
        return f"{self.nome} faz {self.barulho}!"

    def se_movimentar(self):
        return f"{self.nome} se move {self.movimento}."
    
    def alimentar(self):
        return f"{self.nome} foi alimentado às {self.horas_alimentacao}."
    
    def __str__(self):
        return f"{self.nome}, {self.idade} anos, {self.alimentacao}, Habitat: {self.habitat}"

class Mamifero(Animal):
    def __init__(self, nome, idade, barulho, movimento, alimentacao, habitat, horas_alimentacao, tipo_pelo):
    
        Animal.__init__(self, nome, idade, barulho, movimento, alimentacao, habitat, horas_alimentacao)
        self.tipo_pelo = tipo_pelo

    def __str__(self):
        return Animal.__str__(self) + f", Tipo de Pelo: {self.tipo_pelo}"
    
class Ave(Animal):
    def __init__(self, nome, idade, barulho, movimento, alimentacao, habitat, horas_alimentacao, envergadura_asas):
        Animal.__init__(self, nome, idade, barulho, movimento, alimentacao, habitat, horas_alimentacao)
        self.envergadura_asas = envergadura_asas

    def __str__(self):
        return Animal.__str__(self) + f", Envergadura das Asas: {self.envergadura_asas} cm"

class Reptil(Animal):
    def __init__(self, nome, idade, barulho, movimento, alimentacao, habitat, horas_alimentacao, tipo_pele):
        Animal.__init__(self, nome, idade, barulho, movimento, alimentacao, habitat, horas_alimentacao)
        self.tipo_pele = tipo_pele

    def __str__(self):
        return Animal.__str__(self) + f", Tipo de Pele: {self.tipo_pele}"
