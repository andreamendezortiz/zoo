class Animals:
    def __init__(self, name, age, health, happiness):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness
    
    def display_info(self):
        print(f"name: {self.name}, age: {self.age}, health: {self.health}, happiness: {self.happiness}")
        return self

    def feed(self, feed): #aumentar salud y felicidad en 10
        self.health += feed * 0.1
        self.happiness += feed * 0.1
        return self


class Feline(Animals):
    def __init__(self, name, age=2, health=80, happiness=70, teeth=30):
        super().__init__(name, age, health, happiness)
        self.teeth = teeth

    def feed(self):
        self.health += 5
        self.happiness += 10
        return self



class Mammal(Animals):
    def __init__(self, name, age=1, health=85, happiness=60, tail=True):
        super().__init__(name, age, health, happiness)
        self.tail = tail
    
    def feed(self):
        self.health += 10
        self.happiness += 5
        return self




class Fish(Animals):
    def __init__(self, name, age=1, health=60, happiness=70, river=True):
        super().__init__(name, age, health, happiness)
        self.river = river

    def feed(self):
        self.health += 10
        self.happiness += 10
        return self



class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_feline(self, name):
        self.animals.append(Feline(name))
    def add_fish(self, name):
        self.animals.append(Fish(name))
    def add_mammal(self, name):
        self.animals.append(Mammal(name))
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()

zoo1 = Zoo("Buin's Zoo")
zoo1.add_feline('tigre')
zoo1.add_fish('trucha')
zoo1.add_mammal('jirafa')
zoo1.print_all_info()


while True:
    result = input("Seleccione una opción \n 1:agregar un felino\n 2:agregar un pez\n 3:agregar un mamífero\n 4:alimentar a un animal\n 5:mostrar info del zoológico\n 6:salir\n")

    if result == '0':
        break

    elif result == '1':
        print('Seleccionaste un felino')
        tipo = input('¿Qué animal es?')
        nombre = input(f'¿Qué nombre deseas ponerle al {tipo}?')
        zoo1.add_feline(nombre)
        print(f'{tipo} {nombre} fue agregado')
        # import pdb; pdb.set_trace()

    elif result == '2':
        print('Seleccionaste un pez')
        tipo = input('¿Qué animal es?')
        nombre = input(f'¿Qué nombre deseas ponerle al {tipo}?')
        zoo1.add_fish(nombre)
        print(f'{tipo} {nombre} fue agregado')

    elif result == '3':
        print('Seleccionaste un mamífero')
        tipo = input('¿Qué animal es?')
        nombre = input(f'¿Qué nombre deseas ponerle al {tipo}?')
        zoo1.add_mammal(nombre)
        print(f'{tipo} {nombre} fue agregado')

    elif result == '4':
        print('Seleccionaste alimentar un animal:')
        alimentar = input('¿Qué tipo de animal deseas alimentar? \n 1:felino \n 2:pez \n 3:mamífero')
        print(f'tu animal seleccionado ha sido alimentado')
    
    elif result == '5':
        print(zoo1)

    elif result == '6':
        print('Saliste del menú')

    
