from abc import ABC,abstractmethod
import math

from traitlets import TraitError

#1
"""
1. Գրել Animal ծնող class՝ eat() և sleep() մեթոդներով:
   - Այս մեթոդներից յուրաքանչյուրը պետք է վերադարձնի համապատասխան հաղորդագրություն, երբ կանչ է արվում։
   - eat()-ը պետք է վերադարձնի "Animal is eating..." հաղորդագրությունը
   - sleep()-ը պետք է վերադարձնի "Animal is sleeping..." հաղորդագրությունը
   Ծրագիրը պետք է ներառի նաև երկու ժառանգ class-ներ, որոնք ժառանգում են Animal class-ը՝ Bird և Fish:
   Այս class-ները Animal class-ից պետք է ժառանգեն sleep() մեթոդը, բայց նաև պետք է ներառեն իրենց մեթոդները՝ ներկայացնելու համար կենդանիներին բնորոշ վարքագիծը:
   - Bird class-ում, փոփոխեք eat() մեթոդը՝ "Bird is pecking at its food..." հաղորդագրությունը վերադարձնելու համար։
   - Բացի այդ, ներառեք fly() մեթոդը, որը վերադարձնում է "Bird is flying..." հաղորդագրությունը:
   - Fish class-ում ներառեք swim() մեթոդը, որը վերադարձնում է "Fish is swimming..." հաղորդագրությունը:
"""
# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def eat(self):
#         print(f"{self.name} is eating")
#     def sleep(self):
#         print(f"{self.name} is sleeping")
#
#
# class Bird(Animal):
#     def eat(self):
#         print(f"{self.name} is pecking at its food")
#         super().sleep()
#     def fly(self):
#         print(f"{self.name} is flying")
#
#
# class Fish(Animal):
#     def swim(self):
#         print(f"{self.name} is swimming")
#         super().sleep()
#
# a=Animal("Cat")
# a.eat()
# a.sleep()
# b=Bird("Parrot")
# b.eat()
# b.fly()
# f=Fish("Goldfish")
# f.swim()


#2
"""
Գրել Shape abstract class, որը․
   - կունենա __init__(), perimetr(), area() աբստրակտ մեթոդներ։
   Գրել Circle class, որը կժառանգի Shape class-ից, որը․
   - __init__() -ում կընդունի շրջանագծի շառավիղը,
   - մինչ ինիցիալիզացնելը, կստուգի, որ ընդունված արգումենտը ճիշտ մուտքագրված լինի (պետք է լինի դրական թիվ),
   - կվերախմբագրի Shape class-ի perimetr() և area() մեթոդները շրջանագծի համար։
   Գրել Rectangle class, որը կժառանգի Shape class-ից, որը․
   - __init__() -ում կընդունի ուղղանկյան լայնությունը և երկարությունը,
   - մինչ ինիցիալիզացնելը, կստուգի, որ ընդունված արգումենտները ճիշտ մուտքագրված լինեն (պետք է լինեն դրական թվեր),
   - կվերախմբագրի Shape class-ի perimetr() և area() մեթոդները ուղղանկյան համար։
   Գրել Triangle class, որը կժառանգի Shape class-ից, որը․
   - __init__() -ում կընդունի 
     -- կամ եռանկյան երեք կողմերը,
     -- կամ մեկ կողմը և բարձրությունը,
     -- կամ երկու կողմերը և այդ կողմերի կազմած անկյունը, 
   - մինչ ինիցիալիզացնելը, կստուգի, որ ընդունված արգումենտները ճիշտ մուտքագրված լինեն,
   - կվերախմբագրի Shape class-ի perimetr() մեթոդը եռանկյան համար,
   - եռանկյան մակերեսը կհաշվի 3 տարբերակով, կախված մուտքագրված պարամետրերից․
     1) S = (p * (p - a) * (p - b) * (p - c)) ^ 0.5   , որտեղ a, b, c - եռանկյան կողմերն են, p - եռանկյան կիսապարագիծը,
     2) S = a * h / 2                                 , որտեղ a - եռանկյան կողմը, h = եռանկյան բարձրությունը,
     3) S = a * b * sin(alpha) / 2                    , որտեղ a, b - եռանկյան կողմերն են, alpha - եռանկյան a և b կողմերի կազմած անկյունը։
"""

# class Shape():
#     @abstractmethod
#     def __init__(self):
#         pass
#     @abstractmethod
#     def perimetr(self):
#         pass
#     @abstractmethod
#     def area(self):
#         pass
# class Circle(Shape):
#     def __init__(self,r):
#         if r<=0:
#             raise ValueError("r must be positive ")
#         self.r=r
#     def perimetr(self):
#         c=2*math.pi*self.r
#         return c
#     def area(self):
#         s=math.pi*self.r**2
#         return s
#
# class Rectangle(Shape):
#     def __init__(self,l,w):
#         if l<=0 or w<=0:
#             raise ValueError("l and w must be positive ")
#         self.l=l
#         self.w=w
#     def perimetr(self):
#         p=(self.l+self.w)*2
#         return p
#     def area(self):
#         s=self.l*self.w
#         return s
#
#
# class Triangle(Shape):
#     def __init__(self,a,b,c):
#         if not (a + b > c and a + c > b and c + b > a):
#                raise  ValueError("invalid triangle sides")
#         self.a=a
#         self.b=b
#         self.c=c
#     def perimetr(self):
#         p=self.a+self.b+self.c
#         return p
#     def area(self):
#         p=self.perimetr()/2
#         s=(p*(p-self.a)*(p-self.b)*(p-self.c))**0.5
#         return s
#
#
# t=Triangle(3,4,5)
# print(t.perimetr())
# print(t.area())
# c=Circle(5)
# print(c.perimetr())
# print(c.area())
# r=Rectangle(4,5)
# print(r.area())
# print(r.perimetr())



#1

