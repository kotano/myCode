#!/usr/bin/python3
import random

"""Лото

   Правила игры в лото.

   Игра ведется с помощью специальных карточек, на которых отмечены числа, 
   и фишек (бочонков) с цифрами.

   Количество бочонков — 90 штук (с цифрами от 1 до 90).

   Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
   расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

   --------------------------
      9 43 62          74 90
   2    27    75 78    82
      41 56 63     76      86 
   --------------------------

   В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
   случайная карточка. 

   Каждый ход выбирается один случайный бочонок и выводится на экран.
   Также выводятся карточка игрока и карточка компьютера.

   Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
   Если игрок выбрал "зачеркнуть":
      Если цифра есть на карточке - она зачеркивается и игра продолжается.
      Если цифры на карточке нет - игрок проигрывает и игра завершается.
   Если игрок выбрал "продолжить":
      Если цифра есть на карточке - игрок проигрывает и игра завершается.
      Если цифры на карточке нет - игра продолжается.
      
   Побеждает тот, кто первый закроет все числа на своей карточке.

   Пример одного хода:

   Новый бочонок: 70 (осталось 76)
   ------ Ваша карточка -----
   6  7          49    57 58
      14 26     -    78    85
   23 33    38    48    71   
   --------------------------
   -- Карточка компьютера ---
   7 87     - 14    11      
         16 49    55 88    77    
      15 20     -       76  -
   --------------------------
   Зачеркнуть цифру? (y/n)

   Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
   с помощью функции-генератора.

   Подсказка: для работы с псевдослучайными числами удобно использовать 
   модуль random: http://docs.python.org/3/library/random.html

   """

l = list(range(1, 91))
lot = list(range(1, 91))

def make_cards(name=''):
   def aim():
      res = l.pop(l.index(random.choice(l)))
      return res
      
   vals = []
   for x in range(15):
      vals.append(aim())
   vals.sort()
   
   result = ('----{name}----\n{}\n{}\n{}\n------------------'.format(str(vals[0:5]).strip('[]'),str(vals[5:10]),str(vals[10:15]), name=name))
   return result


player = make_cards('Ваша карточка')
comp = make_cards('Карточка компьютера')

while player.count('X')!=15 or comp.count('X')!=15:
   bingo = lot.pop(lot.index(random.choice(lot)))
   print('Новый бочонок: {} (осталось {})'.format(bingo, len(lot)))
   print(player)
   print(comp)

   search = str(bingo)
   answer = input('Зачеркнуть цифру? (y/n)')
   if answer == 'q':
      break

   if len(search)>1:    #check if length of number is more than 1
      if search in player and answer.lower() == 'y':
         player = player.replace(search, 'X')   

      if search in comp:
         comp = comp.replace(search, 'X')
###
# Нужно решить проблему с заменой однозначного числа(когда находит однозначное число заменяются цифры в двузначных)
# Думаю нужно сделать class для make_cards и сделать так, чтобы список отрисовывался каждый раз заново, а не итерироваться по уже созданной строке.

   else:
      if search in player and answer.lower() == 'y':
         ind1 = player.find(search)
         if not player[ind1-1].isdigit():
            player = player.replace(search, 'X')   

      if search in comp:
         ind2 = player.find(search)          #костыль не работает :)
         if not comp[ind2-1].isdigit():      #
            comp = comp.replace(search, 'X') 
      # if search in comp:
      #    ind2 = player.find(search)
      #    if not comp[ind2-1].isdigit:
      #       comp = comp.replace(search+',', 'X')


   print(player)
   print(comp)
   





if __name__ == "__main__":
   pass
   # game()
