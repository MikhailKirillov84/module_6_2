# В этой задаче мы реализуем классы транспорта, в которых нельзя будет просто так поменять цвет,
# мощность двигателя и прочие свойства, т.к. в реальной жизни это чаще всего делается не владельцем, а в специальных сервисах.
# Да, узнать значения этих свойств мы сможем, но вот изменить - нет.

# Вам необходимо создать 2 класса: Vehicle и Sedan, где Vehicle - это любой транспорт, а Sedan(седан) - наследник класса Vehicle.

# создание класса "Vehicle", который имеет один атрибут "__COLOR_VARIANTS"
class Vehicle:
    # создадим атрибут, в который записан список допустимых цветов для окрашивания
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    # создадим метод "__init__"(конструктор), который принимает несколько атрибутов
    def __init__(self, owner, __model, __engine_power, __color):
        # атрибут owner(str) - владелец транспорта, может меняться
        self.owner = owner
        # атрибут __model(str) - модель (марка) транспорта, не может(__) меняться вручную
        self.__model = __model
        # атрибут __engine_power(int) - мощность двигателя, не может(__) меняться
        self.__engine_power = __engine_power
        # атрибут __color(str) - название цвета, не может(__) меняться вручную
        self.__color = __color

    # создадим метод "get_model", который при вызове будет возвращать(return) строку(надпись)
    def get_model(self):
        return f'Модель: {self.__model}'

    # создадим метод "get_horsepower", который при вызове будет возвращать(return) строку(надпись)
    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    # создадим метод "get_color", который при вызове будет возвращать(return) строку(надпись)
    def get_color(self):
        return f'Цвет: {self.__color}'

    # создадим метод "print_info", который при вызове будет выводить результат методов
    def print_info(self):
        # выводим результат метода "get_model" класса "Vehicle"
        print(Vehicle.get_model(self))
        # выводим результат метода "get_horsepower" класса "Vehicle"
        print(Vehicle.get_horsepower(self))
        # выводим результат метода "get_color" класса "Vehicle"
        print(Vehicle.get_color(self))
        # выводим строку с атрибутом "owner" класса "Vehicle"
        print(f'Владелец: {self.owner}')

    # создадим метод "set_color", который принимает один атрибут и создает условие
    def set_color(self, new_color):
        # присваиваем атрибуту значение передаваемое при вызове метода "set_color"
        self.new_color = new_color

        # условие если передаваемое значение атрибута "new_color" есть в списке атрибута "__COLOR_VARIANTS" класса "Vehicle"
        # проверка в "__COLOR_VARIANTS" происходит не учитывая верхний(lower()) регистр ('BLACK' ~ 'black')
        if new_color.lower() in self.__COLOR_VARIANTS:
            # присваиваем атрибуту "self.__color" значение атрибута "new_color"
            self.__color = new_color

        # если же значение атрибута "new_color" нет в списке атрибута "__COLOR_VARIANTS" класса "Vehicle"
        else:
            # выводим строку
            print(f'Нельзя сменить цвет на {new_color}')

# создание класса "Sedan", который имеет свой один атрибут и наследует методы и атрибуты родительского класса "Vehicle"
class Sedan(Vehicle):
    # создадим атрибут "__PASSENGERS_LIMIT" класса "Sedan", который принимает значение
    __PASSENGERS_LIMIT = 5

# создадим объект класса
vehicle1 = Sedan('Fedor', 'Toyota Mark II', 500, 'blue')
# вызываем метод "print_info()" для объекта "vehicle1"
vehicle1.print_info()

# Меняем свойства (в т.ч., вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# проверяем что поменялось, вызываем метод "print_info()" для объекта "vehicle1"
vehicle1.print_info()


