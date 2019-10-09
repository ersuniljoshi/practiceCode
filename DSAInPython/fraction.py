class Fraction(object):
    '''
    Fraction class implementation
    '''
    def __init__(self, top, bottom):
        gcdboth = self.gcd(top, bottom)
        self.num = top//gcdboth
        self.den = bottom//gcdboth

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, other):
        newnum = self.num*other.den + self.den*other.num
        newden = self.den*other.den
        return Fraction(newnum, newden)

    def __sub__(self, other):
        newnum = self.num*other.den - self.den*other.num
        newden = self.den*other.den
        return Fraction(newnum, newden)

    def __div__(self, other):
        newnum = self.num * other.den
        newden = self.den * other.num
        return Fraction(newnum, newden)

    def __mul__(self, other):
        newnum = self.num*other.num
        newden = self.den*other.den
        return Fraction(newnum, newden)

    def __eq__(self, other):
        return self.num*other.den == self.den*other.num

    def gcd(self, n1, n2):
        while n2:
            n1, n2 = n2, n1 % n2
        return n1

f1 = Fraction(1, 2)
f2 = Fraction(2, 4)
print(f1 + f2)
print(f1 - f2)
print(f1 * f2)
print(f1 == f2)
