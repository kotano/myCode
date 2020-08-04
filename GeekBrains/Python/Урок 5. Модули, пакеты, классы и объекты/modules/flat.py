#!/usr/bin/python3
# -*- coding: utf-8 -*-

import math

""" Ремонт в квартире 

  Есть квартира (2 комнаты и кухня). В квартире планируется ремонт: нужно 
  поклеить обои, покрасить потолки и положить пол.

  Необходимо рассчитать стоимость материалов для ремонта.

  Из описания следуют следующие классы:
  = Строительные материалы
    = Обои
    = Потолочная краска
    = Ламинат
  = Комната
  = Квартира

  Подробнее, с методами (+) и атрибутами (-):
  = Строительные материалы
    - площадь (кв. м)
    - цена за единицу (рулон, банку, упаковку)
    = Обои
      - ширина рулона
      - длина рулона
    = Потолочная краска
      - вес банки
      - расход краски
    = Ламинат
      - длина доски
      - ширина доски
      - кол-во досок в упаковке
  = Комната
    - ширина
    - высота
    - длина
    - ширина окна
    - ширина двери
    + поклеить обои
    + покрасить потолок
    + положить пол
    + посчитать смету на комнату
    + при создании комнаты сразу передавать все атрибуты в конструктор __init__()
  = Квартира
    - комнаты
    + добавить комнату
    + удалить комнату
    + посчитать смету на всю квартиру
    + при создании можно передать сразу все комнаты в конструктор

  Необходимо создать стройматериалы, назначить им цены и размеры.
  Создать комнаты, поклеить, покрасить и положить все на свои места.
  Cоздать квартиру, присвоить ей комнаты и посчитать общую смету.

  Подсказка: для округления вверх и вниз используйте:
  import math
  math.ceil(4.2)  # 5
  math.floor(4.2) # 4

  Примечание: Для простоты, будем считать, что обои над окном и над дверью 
  не наклеиваются.
  ----------------

  Дополнительно:
  Сделать у объекта квартиры метод, выводящий результат в виде сметы:

  [Комната: ширина: 3 м, длина: 5 м, высота: 2.4 м]
  Обои        400x6=2400 руб.
  Краска     1000x1=1000 руб.
  Ламинат     800x8=6400 руб.
  [Комната: ширина: 3 м, длина: 4 м, высота: 2.4 м]
  Обои        400x5=2000 руб.
  Краска     1000x1=1000 руб.
  Ламинат     800x7=5600 руб.
  [Кухня: ширина: 3 м, длина: 3 м, высота: 2.4 м]
  Обои        400x4=1600 руб.
  Краска     1000x1=1000 руб.
  Ламинат     800x5=4000 руб.
  ---------------------------
  Итого: 25000 руб.

  """

class Materials:
  def __init__(self, price, length, width):
    self.price = price
    self.length = length
    self.width = width

    self.use = self.length * self.width


class Wallpapers(Materials):
  def __init__(self, price, length, width):
    super().__init__(price, length=10, width=1)

class Paint_tins(Materials):
  def __init__(self, price, weight, waste):
    super().__init__(price, 0, 0)
    self.weight = weight
    self.waste = waste    # waste shows how much surface can be painted with 1 litre of paint
    self.use = self.waste * self.weight

class Laminat(Materials):
  def __init__(self, price, amount, length, width):
    super().__init__(price, length=2, width=0.5)
    self.amount = amount

    self.use = self.length * self.width * self.amount

class Room:
  def __init__(self, length, width, height, win_width=2, door_width=1.5):   #why is there a problem if not set default value for "door_width"?
    self.length = length
    self.width = width
    self.height = height
    self.win_width = win_width
    self.door_width = door_width
  
    self.floor_area = self.length * self.width
    self.ceiling_area = self.floor_area
    self.wall_area = (self.length * self.height) + (self.width * self.height) - (self.win_width * self.height + self.door_width * self.height)  # minus door and window

    self.estimate_cost = []

  # def __str__(self):
  #   return ('Room name: ' + self.name)

  def get_info(self):
    print('Floor area = {}\nCeiling area = {}\nWall area = {}'.format(self.floor_area, self.ceiling_area, self.wall_area))

  def glue_wallpaper(self, material):
    # return material.use - self.wall_area
    cost = material.price * math.ceil(self.wall_area / material.use)
    self.estimate_cost.append(cost)
    return cost

  def paint_ceiling(self, material):
    cost = material.price * math.ceil(self.ceiling_area / material.use)
    self.estimate_cost.append(cost)
    return cost

  def put_floor(self, material):
    cost = material.price * math.ceil(self.floor_area / material.use)
    self.estimate_cost.append(cost)
    return cost

  def count_price(self, *args):
    # return self.glue_wallpaper(args[0]) + self.paint_ceiling(args[1]) + self.put_floor(args[2])
    return sum(self.estimate_cost)

class Apartments:
  def __init__(self, *rooms):
    # for x in rooms:
    #   if type(x) == "<class 'object'>"
    self.rooms = list(rooms)
    self.total_cost = []

  def add_room(self, *args):
    self.rooms.append(args)

  def create_room(self, length, width, height, win_width, door_width):
    Room.__init__(self, length, width, height)
    self.rooms.append(self.__name__)  # may be a problem

  def count_total_price(self):
    for room in self.rooms:
      self.total_cost.append(room.count_price())
    return sum(self.total_cost)

  # def show info      

  def delete_room(self):
    pass

walp = Wallpapers(2000, 10, 2)
tin = Paint_tins(1000, 2, 20)  #price weight waste
lam = Laminat(1500, 20, 2.5, 0.4)

kitchen = Room(6, 4, 3.5)
bedroom = Room(5, 4, 3.5)
childroom = Room(4, 4, 3.5)

kitchen.glue_wallpaper(walp)
kitchen.paint_ceiling(tin)
kitchen.put_floor(lam)
bedroom.glue_wallpaper(walp)
bedroom.paint_ceiling(tin)
bedroom.put_floor(lam)
childroom.glue_wallpaper(walp)
childroom.paint_ceiling(tin)
childroom.put_floor(lam)

aparts = Apartments(kitchen, bedroom, childroom)
# print(aparts.rooms)

print(kitchen.get_info(), kitchen.estimate_cost)
print(kitchen)
print(bedroom.get_info(), bedroom.estimate_cost)
print(childroom.get_info(), childroom.estimate_cost)

print('Kitchen TOTAL COST = ', kitchen.count_price())
print('Bedroom TOTAL COST = ', bedroom.count_price())
print('Childroom TOTAL COST = ', childroom.count_price())

print('Total apartments renovation costs: ' , aparts.count_total_price())
  def myfunc()
