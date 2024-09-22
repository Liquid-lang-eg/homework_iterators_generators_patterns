from abc import ABC

# Задание 1

def generate_fibonacci_sequence(last_num):
    num_1, num_2 = 0, 1
    for i in range(last_num):
        yield num_1
        num_1, num_2 = num_2, num_1 + num_2

while True:
    try:
        num_for_fibonacci = int(input('Введите целочисленное значение; '))
        break
    except ValueError as err:
        error = str(err).split("'")[1]
        print(f"Вы ввели некорректное значение {error}"
              f"Пожалуйста, введите int")

for num in generate_fibonacci_sequence(num_for_fibonacci):
    print(num)

# Задание 2

def generate_endless_sequence(size):
    counter = 1
    for _ in range(size):
        yield counter
        counter += 1
        if counter > 3:
            counter = 1

while True:
    try:
        num_for_sequence = int(input('Введите целочисленное значение; '))
        break
    except ValueError as err:
        error = str(err).split("'")[1]
        print(f"Вы ввели некорректное значение {error}"
              f"Пожалуйста, введите int")
print(generate_endless_sequence(3))
for num in generate_endless_sequence(num_for_sequence):
    print(num)

# Задание 3


class Pizza:

    def __init__(self):
        self.size = None
        self.cheese = None
        self.pepperoni = None
        self.mushrooms = None
        self.onions = None
        self.bacon = None

    def __str__(self):
        return f'Размер пиццы: {self.size}см, сыр в пицце: {self.cheese}, ' \
               f'Pepperoni в пицце: {self.pepperoni}, Грибы в пицце: {self.mushrooms}, ' \
               f'Лук в пицце {self.onions}, Bacon в пицце: {self.bacon}'

class PizzaBuilder(ABC):

    def __init__(self):
        self.pizza = Pizza()

    def set_pizza_size(self):
        pass

    def set_pizza_cheese(self):
        pass

    def is_pepperoni(self):
        pass

    def is_mushrooms(self):
        pass

    def is_onions(self):
        pass

    def is_bacon(self):
        pass

    def get_pizza(self):
        return self.pizza


class MargaritaBuilder(PizzaBuilder):

    def set_pizza_size(self):
        self.pizza.size = 35
        return self

    def set_pizza_cheese(self):
        self.pizza.cheese = 'Parmesan'
        return self

    def is_pepperoni(self):
        self.pizza.pepperoni = False
        return self

    def is_mushrooms(self):
        self.pizza.mushrooms = False
        return self

    def is_onions(self):
        self.pizza.onions = True
        return self

    def is_bacon(self):
        self.pizza.bacon = False
        return self

class PepperoniBuilder(PizzaBuilder):

    def set_pizza_size(self):
        self.pizza.size = 30
        return self

    def set_pizza_cheese(self):
        self.pizza.cheese = 'Mozzarella'
        return self

    def is_pepperoni(self):
        self.pizza.pepperoni = True
        return self

    def is_mushrooms(self):
        self.pizza.mushrooms = False
        return self

    def is_onions(self):
        self.pizza.onions = True
        return self

    def is_bacon(self):
        self.pizza.bacon = False
        return self

class MixedPizzaBuilder(PizzaBuilder):

    def set_pizza_size(self):
        self.pizza.size = 30
        return self

    def set_pizza_cheese(self):
        self.pizza.cheese = 'Parmesan'
        return self

    def is_pepperoni(self):
        self.pizza.pepperoni = True
        return self

    def is_mushrooms(self):
        self.pizza.mushrooms = True
        return self

    def is_onions(self):
        self.pizza.onions = True
        return self

    def is_bacon(self):
        self.pizza.bacon = True
        return self

class Director:

    def __init__(self, builder):
        self.builder = builder

    def make_pizza(self):
        return (self.builder.set_pizza_size()
                .set_pizza_cheese()
                .is_pepperoni()
                .is_mushrooms()
                .is_onions()
                .is_bacon()
                .get_pizza()
                )

builder = MargaritaBuilder()
director = Director(builder)
margarita = director.make_pizza()
print(margarita)

# Задание 4


class Animal(ABC):

    def speak(self):
        pass


class Dog(Animal):

    def speak(self):
        return "WOOF WOOF"

    def __str__(self):
        return f'This is a dog, {self.speak()}'


class Cat(Animal):

    def speak(self):
        return 'MEOW!'

    def __str__(self):
        return f'This is a cat, {self.speak()}'


class AnimalFactory:

    def __init__(self):
        self.animal = None

    def create_animal(self, dog_or_cat):
        """This function takes two possible arguments
        argument dog or argument cat, and creates an object of a class"""
        if dog_or_cat == 'dog':
            self.animal = Dog()
            return self.animal
        elif dog_or_cat == 'cat':
            self.animal = Cat()
            return self.animal
        else:
            return 'Такое животное создать невозможно'


factory = AnimalFactory()
print(factory.create_animal("dog"))
print(factory.create_animal("cat"))
print(factory.create_animal("wolf"))

# Задание 5


class BasicStrategy(ABC):

    @staticmethod
    def execute(a: float, b: float):
        pass


class AdditionStrategy(BasicStrategy):

    @staticmethod
    def execute(a: float, b: float):
        return a + b


class SubtractionStrategy(BasicStrategy):

    @staticmethod
    def execute(a: float, b: float):
        return a - b


class MultiplicationStrategy(BasicStrategy):

    @staticmethod
    def execute(a: float, b: float):
        return a * b


class DivisionStrategy(BasicStrategy):

    @staticmethod
    def execute(a: float, b: float):
        try:
            return a / b
        except ZeroDivisionError:
            return 0


class Calculator:

    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy: BasicStrategy):
        self.strategy = strategy
        return self

    def calculate(self, a: float, b: float):
        return self.strategy.execute(a, b)


new_strategy = SubtractionStrategy()
calculator = Calculator()
print(calculator.set_strategy(new_strategy).calculate(12, 2))


