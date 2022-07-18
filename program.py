def fahrenheit_to_celsius(fahren):
    celsius = (fahren - 32) * (5/9)
    celsius = round(celsius, 3)
    return celsius

temp = 98.6

print(fahrenheit_to_celsius(temp))