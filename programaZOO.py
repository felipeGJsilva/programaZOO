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
