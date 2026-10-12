# What is this "Converter" converting?!?
"""This "Converter" is converting Fahrenheit-to-Celsius"""
class Converter:
    """Class representing a Fahrenheit-to-Celsius Converter"""
    def __init__(self, factor, offset):
        self.factor = factor
        self.offset = offset

    def convert(self, value):
        """A function that return the math equation to convert Fahrenheit-to-Celsius"""
        return value * self.factor + self.offset


# Why such oddly specific numbers?!?
# And why "5/9" twice?!?
c = Converter(5/9, -32 * 5/9)
print(c.convert(212))
