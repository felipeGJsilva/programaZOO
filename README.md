# programaZOO

class Animal:
    def __init__(self, nome, idade, barulho, movimento, alimentacao, habitat, horas_alimentacao):
        self.nome = nome
        self.idade = idade
        self.barulho = barulho
        self.movimento = movimento
        self.alimentacao = alimentacao
        self.habitat = habitat
        self.vizinhos = []
        self.horas_alimentacao = horas_alimentacao

    def adicionar_vizinho(self, vizinho):
        if len(self.vizinhos) < 2:
            self.vizinhos.append(vizinho)
        else:
            print(f"{self.nome} já tem o número máximo de vizinhos.")

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
        super().__init__(nome, idade, barulho, movimento, alimentacao, habitat, horas_alimentacao)
        self.tipo_pelo = tipo_pelo

    def __str__(self):
        return super().__str__() + f", Tipo de Pelo: {self.tipo_pelo}"
