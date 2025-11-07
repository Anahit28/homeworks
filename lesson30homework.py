#1

"""
Գրել Calculator class, որը․
   - __init__ ում կստանա թիվ և կստուգի այդ թվի int կամ float լինելը, հակառակ դեպքում կվերադարձնի Error,
   - կունենա միայն getter մեթոդ տրված թիվը ստանալու համար, իսկ այդ թիվը կլինի private,
   - կունենա համապատասխան magic մեթոդներ հետևյալ գործողությունների համար (+, -, *, /, //, %, **),
   - կունենա համապատասխան magic մեթոդներ հետևյալ գործողությունների համար (+=, -=, *=, /=, //=, %=, **=),
   - կունենա համապատասխան magic մեթոդներ հետևյալ գործողությունների համար (==, >, >=, <, <=, !=),
   - վերոնշյալ մեթոդները ռեալիզացված կլինեն այնպես, որ աշխատեն նաև Calculator կլասի երկու օբյեկտների համար,
   - կունենա համապատասխան magic մեթոդներ, որոնք թույլ կտան օբյեկտը տպելուց․ ստանալ թիվը (__str__), ստանալ թիվը և թվի տիպը (__repr__)։
"""
class Calculator:
    def __init__(self,a):
        if not isinstance(a,float|int):
            raise ValueError
        self.__a=a
    @property
    def get_the_value(self):
        return self.__a
    def __add__(self, other):
        if  isinstance(other,Calculator):
            other=other.__a
        return Calculator(self.__a+other)

    def __radd__(self, other):
        if isinstance(other, Calculator):
            other = other.__a
        return self + other

    def __iadd__(self, other):
        if isinstance(other, Calculator):
            other = other.__a
        self.__a+=other
        return self
    def __sub__(self, other):
        if  isinstance(other,Calculator):
            other=other.__a
        return Calculator(self.__a - other)

    def __rsub__(self, other):
        if isinstance(other, Calculator):
            other = other.__a
        return Calculator(other - self.__a)

    def __isub__(self, other):
        if isinstance(other, Calculator):
            other = other.__a
        self.__a-=other
        return self

    def __mul__(self, other):
        if isinstance(other, Calculator):
            other = other.__a
        return Calculator(self.__a * other)

    def __rmul__(self, other):
        if isinstance(other, Calculator):
            other = other.__a
        return self * other

    def __imul__(self, other):
        if isinstance(other, Calculator):
            other = other.__a
        self.__a *= other
        return self

    def __truediv__(self, other):
        if other == 0:
            raise ZeroDivisionError("division by zero")
        if isinstance(other, Calculator):
            other = other.__a
        return Calculator(self.__a / other)

    def __rtruediv__(self, other):
        if self.__a == 0:
            raise ZeroDivisionError("division by zero")
        if isinstance(other, Calculator):
            other = other.__a
        return Calculator(other/self.__a )

    def __itruediv__(self, other):
        if other == 0:
            raise ZeroDivisionError("division by zero")
        if isinstance(other, Calculator):
            other = other.__a
        self.__a /= other
        return self

    def __floordiv__(self, other):
        if other == 0:
            raise ZeroDivisionError("division by zero")
        if isinstance(other, Calculator):
            other = other.__a
        return Calculator(self.__a // other)

    def __rfloordiv__(self, other):
        if self.__a == 0:
            raise ZeroDivisionError("division by zero")
        if isinstance(other, Calculator):
            other = other.__a
        return Calculator(other // self.__a)

    def __ifloordiv__(self, other):
        if other == 0:
            raise ZeroDivisionError("division by zero")
        if isinstance(other, Calculator):
            other = other.__a
        self.__a //= other
        return self
    def __mod__(self, other):
        if isinstance(other, Calculator):
            other = other.__a
        return Calculator(self.__a % other)

    def __rmod__(self, other):
        if isinstance(other, Calculator):
            other = other.__a
        return Calculator(other % self.__a)

    def __imod__(self, other):
        if isinstance(other, Calculator):
            other = other.__a
        self.__a %= other
        return self

    def __pow__(self, other):
        if isinstance(other, Calculator):
            other = other.__a
        return Calculator(self.__a ** other)

    def __rpow__(self, other):
        if isinstance(other, Calculator):
            other = other.__a
        return Calculator(other ** self.__a)

    def __ipow__(self, other):
        if isinstance(other, Calculator):
            other = other.__a
        self.__a **= other
        return self
    def __eq__(self, other):
        if isinstance(other,Calculator):
            other=other.__a
            return self.__a==other.__a