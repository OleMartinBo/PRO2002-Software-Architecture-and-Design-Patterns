# What is this "Converter" converting?!?
"""This "Converter" is converting Fahrenheit-to-Celsius"""
class FahrenheitConverter:
    """Class representing a Fahrenheit to Celsius Converter"""
    
    # The numbers are specific for the math formula to convert Fahrenheit to Celsius
    def convert(self, fahrenheit):
        """A method that return the math formula to convert Fahrenheit-to-Celsius"""
        return (fahrenheit - 32) * 5/9

# Creates an objet and prints the degrees in Celsius
c = FahrenheitConverter()
print(c.convert(212))
