import random
from math import factorial
#ex3
"""
Create a Computation class with a default constructor (without parameters)
allowing to perform various calculations on integers numbers.
•Create a method called factorial() which allows to calculate the factorial of an
integer.
integers 1 + 2 + 3 + .. + n.
•Create a method called is_prime() allowing to test the primality of a given
integer.
•Create a method called all_is_prime() allowing to display all prime integer
numbers from 2 to n.
•Create a table_mult() method which creates and displays the multiplication
table of a given integer (from 1 to 10).
•Then create an all_tables_mult() method to display all the integer
multiplication tables (from 1 to 10).
"""


# class Computation:
#     def factorial(self, n):
#         if n in (0, 1):
#             return n
#         return n * factorial(n - 1)
#
#     def summ(self, n):
#         summa = 0
#         for i in range(1, n + 1):
#             summa += i
#         return summa
#
#     def is_prime(self, value):
#         for i in range(2, int(value ** 0.5) + 1):
#             if value % i == 0:
#                 return False
#         return True
#
#     def all_is_prime(self, n):
#         lst = []
#         for i in range(2, n):
#             if self.is_prime(i):
#                 lst.append(i)
#         return lst
#
#     def table_mult(self, num):
#         print(" *  ", end="  ")
#         for i in range(1, num):
#             print(f"{i:02d}", end="   ")
#         print()
#         for j in range(1, num):
#             print(f"{j:02d}", end="    ")
#
#             for i in range(1, num):
#                 print(f"{i * j:02d}", end="   ")
#             print()
#
#     def all_table_mult(self):
#         self.table_mult(11)
#
#
# c = Computation()
# print(c.table_mult(5))
# print(c.factorial(4))
# print(c.is_prime(12))
# print(c.all_is_prime(5))
# print(c.summ(6))
# print(c.all_table_mult())




#10-anhuys

#
# class Card:
#
#     def __init__(self, suit, value):
#         self.suit = suit
#         self.value = value
#
#     def __repr__(self):
#         return f"{self.suit[0]}-{self.value}"
#
# class Deck:
#     def __init__(self, number=156):
#         self.number = number
#         s = ("Hearts", "Diamonds", "Clubs", "Spades")
#         v = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
#         self.cards = []
#         for i in s:
#             for j in v:
#                 self.cards.append(Card(i,j))
#
#     def __str__(self):
#         return str(self.cards)
#
#     def shuffle(self):
#         random.shuffle(self.cards)
#
#     def deal(self):
#         return [self.cards.pop() for i in range(2)]
#
#
#
# class Player:
#     def __init__(self,name):
#         self.name=name
#         self.summa= []
#         # self.d = {"A":11 if self.summa<=21 else 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
#         #       "10": 10, "J": 10, "Q": 10, "K": 10}
#         self.bill=[]
#
#     # def BlackJack(self):
#     #     p=Deck.deal
#     #     self.summa+=[i for i in Deck().cards]
#     #     if >:
#     #         print(f"bot: {b}")
#     #         print(f"player: {p}")
#     #
#     #     elif n=="stand":
#     # def play(self):
#     def playing(self):
#         if n=="hit":
#             Deck().deal()
#
#
# bot=Deck.deal
# player=Deck.deal
# print(player)
# print(bot[0])
# n=input("hit or stand")


#8
"""Для данной игры необходимо реализовать механику магии, где при соединении двух
элементов получается новый. 

- У нас есть четыре базовых элемента: «Вода», «Воздух», «Огонь», «Земля».
- Из них как раз и получаются новые: «Шторм», «Пар», «Грязь», «Молния», «Пыль», «Лава».
- Вот таблица преобразований:
  -- Вода + Воздух = Шторм
  -- Вода + Огонь = Пар
  -- Вода + Земля = Грязь
  -- Воздух + Огонь = Молния
  -- Воздух + Земля = Пыль
  -- Огонь + Земля = Лава
- Напишите программу, которая реализует все эти элементы. 
- Каждый элемент необходимо организовать как отдельный класс. Если результат не определён, то возвращается None.
- Примечание: сложение объектов можно реализовывать через магический метод __add__.
- Дополнительно: придумайте свой элемент (или элементы), а также реализуйте его взаимодействие с остальными элементами.
"""
#
#
# class Water:
#
#     def __add__(self, other):
#         if isinstance(other, Soil):
#             return Mud()
#         elif isinstance(other, Fire):
#             return Steam()
#         elif isinstance(other, Air):
#             return Storm()
#
#         else:
#             return None
#
#
# class Air:
#
#     def __add__(self, other):
#         if isinstance(other, Soil):
#             return Dust()
#         elif isinstance(other, Fire):
#             return Lightning()
#         elif isinstance(other, Water):
#             return Storm()
#         else:
#             return None
#
#
# class Fire:
#
#     def __add__(self, other):
#         if isinstance(other, Soil):
#             return Lava()
#         elif isinstance(other, Water):
#             return Steam()
#         elif isinstance(other, Air):
#             return Lightning()
#         else:
#             return None
#
#
# class Soil:
#     def __add__(self, other):
#         if isinstance(other, Water):
#             return Mud()
#         if isinstance(other, Air):
#             return Dust()
#         if isinstance(other, Fire):
#             return Lava()
#         else:
#             return None
#
#
# class Storm:
#     def __add__(self, other):
#         if isinstance(other, Air):
#             return "Storm"
#         else:
#             return None
#
#
# class Steam:
#     def __add__(self, other):
#         if isinstance(other, Fire):
#             return "Steam"
#         else:
#             return None
#
#
# class Mud:
#     def __repr__(self):
#         return "Mud"
#
#
# class Lightning:
#     def __repr__(self):
#         return "Lightning"
#
#
# class Dust:
#     def __repr__(self):
#         return "Dust"
#
#
# class Lava:
#     def __repr__(self):
#         return "Lava"
#
#
# f = Fire()
# s = Soil()
# w = Water()
# a = Air()
# print(f + s)
# print(a + s)
# print(w + s)
# print(s + f)
# print(s + a)
# print(s + w)



#11---
"""
class Cell:
    # Клетка, у которой есть значения
    # - занята она или нет
    # - номер клетки
class Board:
    # Класс поля, который создаёт у себя экземпляры клетки
class Player:
    # У игрока может быть
    # - имя
    # - на какую клетку ходит
"""
class Cell:
    def __init__(self):
        self.value=" "
    def is_empty(self):
        return self.value==" "
class Board:
    def __init__(self):
        self.grid=[[Cell() for _ in range(3)] for _ in range(3)]
    def is_free(self,row,col):
        return self.grid[row][col]==" "



class Player:
    def __init__(self,name,marker):
        self.name=name
        self.marker=marker
        self.row=int(input("Enter the row "))
        self.col=int(input("Enter the column "))
        if board.is_free(self.row,self.col):
            board.grid[self.row][self.col]=marker
        else:
            print("invalid")

cell=Cell()
board=Board()
p1=Player("Ani","X")
p2=Player("Anna","O")
