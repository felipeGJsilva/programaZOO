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
    
class Mamifero(Animal):
    def __init__(self, nome, idade, barulho, movimento, alimentacao, habitat, horas_alimentacao):
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
        print("1. Adicionar animal")
        print("2. Buscar animal") 
        print("3. Listar todos os animais")
        print("4. Listar animais por categoria")

        escolha = input('Escolha uma opção: ')
        
        if escolha == '1':
            tipo_animal = input("Digite o tipo de animal (mamífero - 1, ave - 2, réptil - 3): ")
            nome = input("Digite o nome do animal: ")
            idade = int(input("Digite a idade do animal: "))
            barulho = input("Digite o barulho do animal: ")
            movimento = input("Digite o movimento do animal: ")
            alimentacao = input("Digite a alimentação do animal: ")
            habitat = input("Digite o habitat do animal: ")
            horas_alimentacao = input("Horário de alimentação do animal: ")

            if tipo_animal == "1":
                animal = Mamifero(nome, idade, barulho, movimento, alimentacao, habitat, horas_alimentacao)
            elif tipo_animal == "2":
                animal = Ave(nome, idade, barulho, movimento, alimentacao, habitat, horas_alimentacao)
            elif tipo_animal == "3":
                animal = Reptil(nome, idade, barulho, movimento, alimentacao, habitat, horas_alimentacao)
            else:
                print("Tipo de animal inválido.")
                continue

            animais.append(animal)
            print(f"Animal {animal.nome} adicionado com sucesso!")
            

        elif escolha == '2':
            nome = input("Digite o nome do animal: ")
            for animal in animais:
                  if animal.nome.lower() == nome.lower():
                      print(f"nome = {animal.nome}")
                      print(f"idade = {animal.idade}")
                      print(f"barulho = {animal.barulho}")
                      print(f"idade = {animal.movimento}")
           
        elif escolha == "3":
            for animal in animais:
                print(animal.nome)

        
if __name__ == "__main__":
    main()