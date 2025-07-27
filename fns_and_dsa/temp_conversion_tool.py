FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    answer = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit}°F is {answer}°C")
    
def convert_to_fahrenheit(celsius):
    answer = CELSIUS_TO_FAHRENHEIT_FACTOR * celsius + 32
    print(f"{celsius}°C is {answer}°F")
    
user_input_temp = int(input("Enter the temperature to convert: "))
user_input_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if user_input_unit == 'C':
    convert_to_fahrenheit(user_input_temp)
elif user_input_unit == 'F':
    convert_to_celsius(user_input_temp)
else:
    print("Invalid temperature. Please enter a numeric value.")