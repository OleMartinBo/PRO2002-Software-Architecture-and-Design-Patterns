# What is this "Converter" converting?!?
"""This "Converter" is converting Fahrenheit-to-Celsius"""
class FahrenheitConverter:
    """Class representing a Fahrenheit to Celsius Converter"""

    def convert(self, fahrenheit):
        """A method that return the math formula to convert Fahrenheit-to-Celsius"""
        return (fahrenheit - 32) * 5/9


# Why such oddly specific numbers?!?
# The numbers are specific for the math formula to convert Fahrenheit to Celsius

# And why "5/9" twice?!?
# The factor is (5/9) and the is offset (-32 * 5/9).
# Therefore are both are used to to convert fahrenheit.
#c = Converter(5/9, -32 * 5/9)
#print(c.convert(212))

# Creates an objet and prints the degrees in Celsius
c = FahrenheitConverter()
print(c.convert(212))
