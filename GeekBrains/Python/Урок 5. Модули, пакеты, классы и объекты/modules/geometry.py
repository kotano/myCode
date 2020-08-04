#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    Это пример небольшой программы для рисования кругов и квадратов.
    Вам нужно на основе этой программы сделать небольшую "танцевальную" сценку с
    использованием кругов, квардратов и треугольников. Сделать всё это нужно в
    объектно ориентированном стиле.

    Какие классы нужно реализовать:

    -Многоугольник(на его основе сделать квадрат и правильный треугольник)
    --класс должне уметь отрисовывать себя
    --премещаться в некоторм направлении заданом координатами x, y
    --увеличивать(необязательно)
    --поворачивать(необязательно)

    -Квардрат(наследуется от многоугольника)
    --метод __init__ принимает координаты середины, ширину и цвет

    -Треугольник(наследуется от многоугольника)
    --метод __init__ принимает координаты середины, длинну грани и цвет

    -Круг
    --метод __init__ принимает координаты середины, радиус и цвет
    --класс должне уметь отрисовывать себя
    --премещаться в некоторм направлении заданом координатами x, y
    --увеличивать(необязательно)

    Также рекомендую создать вспомогательный класс Vector для представления
    точек на плоскости и различных операций с ними - сложение, умножение на число,
    вычитаные.


    Из получившихся классов нужно составить какую-нибудь динамическую сцену.
    Смотрите пример example.gif
    """

import turtle
import time
import random
import math

def draw_rect(ttl):
    x = random.randint(-200, 200) #получаем случайные координаты
    y = random.randint(-200, 200)

    ttl.color('red') #устанавливаем цвет линии
    ttl.penup() # убираем "ручку" от холста, чтобы переместить в нужное место
    ttl.setpos(x, y) # перемещаем на первую вершину
    ttl.pendown() #опускаем ручку обратно
    ttl.goto(x + 50, y) #проводим линии для сторон четырёхугольника
    ttl.goto(x + 50, y + 50)
    ttl.goto(x, y + 50)
    ttl.goto(x, y)

def draw_circle(ttl):
    x = random.randint(-200, 200) #получаем случайные координаты
    y = random.randint(-200, 200)

    ttl.color('violet') #устанавливаем цвет линии
    ttl.penup() # убираем "ручку" от холста, чтобы переместить в нужное место
    ttl.setpos(x, y) # перемещаем в "основание" - это будет самая низкая точка
    ttl.pendown() #опускаем ручку обратно

    ttl.circle(25) #рисуем круг радиуса 25


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __mul__(self, k):
        return Vector(self.x * k, self.y * k)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __div__(self, k):
        return Vector(self.x / k, self.y / k)

    def __repr__(self):
        return 'V({}, {})'.format(self.x, self.y)

class Circle:
    def __init__(self, ttl, x, y, radius, color):
        self.ttl = ttl
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self):
        self.ttl.color(self.color)
        self.ttl.penup()
        self.ttl.setpos(self.x, self.y) #need to determine center
        self.ttl.pendown()
        self.ttl.circle(self.radius)

    def scale(self, k):
        self.radius *= k

    def move(self, x, y):
        self.x += x
        self.y += y

    def rotate(self, angle):
        pass

class Polygon:
    def __init__(self, ttl, vertex_list, color):
        self.vertex_list = vertex_list
        self.color = color
        self.ttl = ttl
        # self.ttl = turtle.Turtle()

    def draw(self):
        
        self.ttl.color(self.color)
        last = self.vertex_list[-1]
        self.ttl.penup()
        self.ttl.setpos(last.x, last.y)
        self.ttl.pendown()
        for v in self.vertex_list:
            self.ttl.goto(v.x, v.y)
        self.ttl.penup()

    def scale(self, point, k):
        for i, v in enumerate(self.vertex_list):
            self.vertex_list[i] = (v - point) * k + point

    def move(self, x, y):
        for i, v in enumerate(self.vertex_list):
            self.vertex_list[i] = v + Vector(x,y)

    def rotate(self, point, angle):
        pass
        for i, v in enumerate(self.vertex_list):
            b = v - point
            # self.vertex_list[i] = Vector(b.)

class RightPoly(Polygon):
    def __init__(self, ttl, vertex_list, color):
        super().__init__(ttl, vertex_list, color)

    def scale(self, k ):
        pass
        super().scale(self._get_center(), k)

    def rotate(self, angle):
        pass
        super().rotate(self._get_center(), angle)


class Rect(RightPoly):
    def __init__(self, ttl, x, y, width, height, color):
        vertex_list = [Vector(x - width/2, y - height/2),
                        Vector(x + width/2, y - height/2),
                        Vector(x + width/2, y + height/2),
                        Vector(x - width/2, y + height/2)]
        super().__init__(ttl, vertex_list, color)

    def get_center(self):
        return (self.vertex_list[0] + self.vertex_list[2]) / 2

class Triangle(RightPoly):
    def __init__(self, ttl,x, y, width, color):
        height = math.sqrt(3) * width / 2
        vertex_list = [Vector(x - width/2, y - height/2),
                        Vector(x + width/2, y - height/2),
                        Vector(x, y + height/2)]
        super().__init__(ttl, vertex_list, color)

    def get_center(self):
        return ((self.vertex_list[0] + self.vertex_list[1]) / 2 + self.vertex_list[2]/2)


screen = turtle.Screen()
turtle.tracer(0, 0)
turtle.hideturtle()

ttl = turtle.Turtle()
ttl.hideturtle()

p1 = Rect(ttl, 0, 0, 100, 100, 'red')

import itertools

c1 = Circle(ttl, 0, 0, 50, 'violet')
# direction = itertools.cycle([1] * 10 + [-1] * 10)
# k = 1.1

scene = [p1, c1]

group1 = [Triangle(ttl, 200, -200, 35, 'orange'), Circle(ttl, 150, -200, 20, 'blue'), Triangle(ttl, 100, -200, 35, 'orange')]

scene.extend(group1)


def demo():
    while True:

        time.sleep(0.2)
        ttl.clear()

        for x in scene:
            x.draw()

        c1.scale(random.randint(10, 20))

        for x in group1:
            x.move(-40, 0)

        turtle.update()


def main():

    turtle.tracer(0, 0) #устанавливаем все задержки в 0, чтобы рисовалось мгновенно
    # turtle.hideturtle() #убираем точку посередине

    ttl = turtle.Turtle() #создаём объект черепашки для рисования
    ttl.hideturtle() #делаем её невидимой

    while True:
        time.sleep(0.5) #засыпаем на полсекунды, чтобы увидеть что нарисовали
        ttl.clear() #очищаем всё нарисованое ранее
        draw_rect(ttl)
        draw_circle(ttl)
        turtle.update() #т.к. мы сделали turtle.tracer(0, 0) нужно обновить экран, чтобы увидеть нарисованное

if __name__ == '__main__':
#     main()
    demo()
    # secondary()
