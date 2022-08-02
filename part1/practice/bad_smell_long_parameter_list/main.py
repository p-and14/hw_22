# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)
class Field:
    def set_unit(self, x, y, unit):
        pass


class Unit:
    def __init__(self, field, status, speed=1):
        self.status = status
        self.speed = speed
        self.field = field

    def move(self, x, y, direction):
        speed = self._get_speed()

        if direction == 'UP':
            self.field.set_unit(x=x, y=y + speed, unit=self)
        elif direction == 'DOWN':
            self.field.set_unit(x=x, y=y - speed, unit=self)
        elif direction == 'LEFT':
            self.field.set_unit(x=x - speed, y=y, unit=self)
        elif direction == 'RIGHT':
            self.field.set_unit(x=x + speed, y=y, unit=self)

    def _get_speed(self):
        if self.status == "fly":
            return self.speed * 1.2
        elif self.status == "crawl":
            return self.speed * 0.5
        else:
            raise ValueError('Неправильные данные')
