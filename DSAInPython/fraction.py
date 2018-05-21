
def gcd(n1, n2):
    while n2:
        n1, n2 = n2, n1%n2
    return n1

class fraction(object):

    def __init__(self, top, bottom):
        gcdboth = gcd(top, bottom)
        self.num = top//gcdboth
        self.den = bottom//gcdboth

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, other):
        newnum = self.num*other.den + self.den*other.num
        newden = self.den*other.den
        return fraction(newnum, newden)


    def __sub__(self, other):
        newnum = self.num*other.den - self.den*other.num
        newden = self.den*other.den
        return fraction(newnum, newden)


    def __div__(self, other):
        newnum = self.num* other.den
        newden = self.den*other.num
        return fraction(newnum, newden)


    def __mul__(self, other):
        newnum = self.num*other.num
        newden = self.den*other.den
        return fraction(newnum, newden)

    def __eq__(self, other):
        return self.num*other.den == self.den*other.num


f1 = fraction(1, 2)
f2 = fraction(2, 4)
print ( f1 + f2 )
print ( f1 - f2 )
print ( f1 * f2 )
print ( f1 // f2 )
print ( f1 == f2 )
