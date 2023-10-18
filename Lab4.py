class MyString:
    def __init__(self, value):
        self.value = value

    def length(self):
        return len(self.value)

    def uppercase(self):
        return self.value.upper()

    def lowercase(self):
        return self.value.lower()

    def reverse(self):
        return self.value[::-1]

    def count_occurrences(self, substring):
        return self.value.count(substring)

def task1():
    my_string = MyString("Hello, World!")

    print("Длина строки:", my_string.length())
    print("Верхний регистр:", my_string.uppercase())
    print("Нижний регистр:", my_string.lowercase())
    print("Обратная строка:", my_string.reverse())
    print("Количество вхождений 'o':", my_string.count_occurrences("o"))

class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        print("Letters in {} alphabet: {}".format(self.lang, self.letters))

    def letters_num(self):
        return len(self.letters)


class EngAlphabet(Alphabet):
    __letters_num = 26

    def __init__(self):
        super().__init__('En', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    def is_en_letter(self, letter):
        return letter.upper() in self.letters

    def letters_num(self):
        return EngAlphabet.__letters_num

    @staticmethod
    def example():
        return "This is an example text in English."

def task2():

    eng_alphabet = EngAlphabet()
    eng_alphabet.print()
    print("Number of letters in English alphabet:", eng_alphabet.letters_num())
    print("Is 'A' an English letter?", eng_alphabet.is_en_letter('A'))
    print("Is 'Ё' an English letter?", eng_alphabet.is_en_letter('Ё'))
    print(EngAlphabet.example())

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Запуск отрисовки с помощью ", self.title)


class Pencil(Stationery):
    def draw(self):
        print("Запуск отрисовки с помощью ", self.title)


class Handle(Stationery):
    def draw(self):
        print("Запуск отрисовки с помощью ", self.title)

def task3():

    pen = Pen("ручки")
    pencil = Pencil("карандаша")
    handle = Handle("маркера")

    pen.draw()
    pencil.draw()
    handle.draw()

class Dog:

    total_dogs = 0

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        Dog.total_dogs += 1


    def display_info(self):
        print("Имя: ", self.name, "Порода: ", self.breed)


    @staticmethod
    def dog_to_human_age(dog_age):
        return dog_age * 7


    @classmethod
    def total_dogs_count(cls):
        return cls.total_dogs

def task4():

    dog1 = Dog("Челси", "Лабрадор")
    dog2 = Dog("Макс", "Франзузский бульдог")
    dog3 = Dog("Лайт", "Шпиц")
    dog4 = Dog("Цали", "Терьер")


    dog1.display_info()
    dog2.display_info()
    dog3.display_info()
    dog4.display_info()


    dog_age = 5
    human_age = Dog.dog_to_human_age(dog_age)
    print(f"Возраст собаки {dog_age} лет соответствует возрасту человека {human_age} лет")


    print("Общее количество собак: ", Dog.total_dogs_count())

def isInt(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
def inputInt(description):
    str = input(description)
    while not isInt(str):
        print("Некорректный ввод, введите только числа из диапазона")
        str = input()
    return int(str)

def main():
    isWork = True

    while isWork:
        print("1. 1 задание, class string")
        print("2. 2 задание, class Alphabet")
        print("3. 3 задание, class Stationery")
        print("4. 4 задание, свой класс Dogs")
        print("5. Выход ")

        match (inputInt("Выберите вариант: ")):
            case 1:
                task1()
            case 2:
                task2()
            case 3:
                task3()
            case 4:
                task4()
            case 5:
                isWork = False
            case _:
                print("Некорректный ввод")

main()