import math
class Fraction:
    """A fraction with a numerator and denominator and arithmetic operations.

    Fractions are always stored in proper form, without common factors in 
    numerator and denominator, and denominator >= 0.
    Since Fractions are stored in proper form, each value has a
    unique representation, e.g. 4/5, 24/30, and -20/-25 have the same
    internal representation.
    """
    
    def __init__(self, numerator, denominator=1):
        """Initialize a new fraction with the given numerator
           and denominator (default 1).
        """
        gcd = math.gcd(numerator, denominator)
        self.numerator = numerator / gcd
        self.denominator = denominator / gcd
        self.fraction = self.numerator / self.denominator
        if denominator == 0:
            self.denominator = math.nan
        elif denominator < 0:
            self.numerator = self.numerator * (-1)
            self.denominator = abs(self.denominator)



    #TODO Write the __add__ method, and remove this TODO comment.
    def __add__(self, frac):
        """Return the sum of two fractions as a new fraction.
           Use the standard formula  a/b + c/d = (ad+bc)/(b*d)
        """
        numerator_sum = (self.numerator * frac.denominator) + (frac.numerator * self.denominator)
        denominator_sum = self.denominator * frac.denominator
        return Fraction(numerator_sum, denominator_sum)

    def __mul__(self, frac):
        """ Return the multiple of two fractions as a new fraction.
            Use the standard formula a / b * c / d = (a * c) / (b * d)
        """
        numerator_mul = (self.numerator * frac.numerator)
        denominator_mul = (self.denominator * frac.denominator)
        return Fraction(numerator_mul, denominator_mul)

    def __str__(self):
        """ Return the fraction to a form of string
        """
        if self.denominator == 1 or self.numerator == 0:
            return str(int(self.numerator))
        else:
            return '{}/{}'.format(int(self.numerator),int(self.denominator))





    #TODO write __mul__ and __str__.  Verify __eq__ works with your code.
    #Optional have fun and overload other operators such as 
    # __sub__ for f-g
    # __gt__  for f > g
    # __neg__ for -f (negation)

    def __eq__(self, frac):
        """Two fractions are equal if they have the same value.
           Fractions are stored in proper form so the internal representation
           is unique (3/6 is same as 1/2).
        """
        return self.numerator/self.denominator == frac.numerator/frac.denominator
