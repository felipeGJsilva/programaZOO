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
      
   
    
class Ave(Animal):
    def __init__(self, nome, idade, barulho, movimento, alimentacao, habitat, horas_alimentacao):
        Animal.__init__(self, nome, idade, barulho, movimento, alimentacao, habitat, horas_alimentacao)
      

   

class Reptil(Animal):
    def __init__(self, nome, idade, barulho, movimento, alimentacao, habitat, horas_alimentacao):
        Animal.__init__(self, nome, idade, barulho, movimento, alimentacao, habitat, horas_alimentacao)
        
def main():

    animais = []
    while True:
        print("  MENU  ")
        print("1. adicinonar animal")
        
        
        escolha = input('Escolha uma opçãO: ')
        
        if escolha == '1':
            tipo_animal = input("digite o tipo de animal (mamifero, ave, reptil): ")
            nome = input("digite o nome do animal: ")
            idade = int(input("digite a idade do animal: "))
            barulho = input("digite o barulho do animal: ")
            movimento = input("digite o movimento do animal: ")
            alimentacao = input("digite a alimentação do animal: ")
            habitat = input("digite o habitat do animal: ")
            horas_alimentacao = input("Horário de alimentação do animal: ")

            if tipo_animal == "mamífero":
                tipo_pelo = input("Tipo de pelo: ")
                animal = Mamifero(nome, idade, barulho, movimento, alimentacao, habitat, horas_alimentacao)
            elif tipo_animal == "ave":
                
                animal = Ave(nome, idade, barulho, movimento, alimentacao, habitat, horas_alimentacao)
            elif tipo_animal == "réptil":
               
                animal = Reptil(nome, idade, barulho, movimento, alimentacao, habitat, horas_alimentacao)
            else:
                print("Tipo de animal inválido.")
                continue

            animais.append(animal)
            print(f"Animal {animal.nome} adicionado com sucesso!")

if __name__ == "__main__":
    main()