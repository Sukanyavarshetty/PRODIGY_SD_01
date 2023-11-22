def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return kelvin * 9/5 - 459.67

def main():
    print("Welcome to Temperature Conversion Program!")
    print("Available units: Celsius, Fahrenheit, Kelvin")

    unit_from = input("Enter the original unit of measurement: ").lower()
    temp = float(input("Enter temperature value: "))

    if unit_from == 'celsius':
        print(f"{temp} Celsius is equivalent to:")
        print(f"{celsius_to_fahrenheit(temp)} Fahrenheit")
        print(f"{celsius_to_kelvin(temp)} Kelvin")
    elif unit_from == 'fahrenheit':
        print(f"{temp} Fahrenheit is equivalent to:")
        print(f"{fahrenheit_to_celsius(temp)} Celsius")
        print(f"{fahrenheit_to_kelvin(temp)} Kelvin")
    elif unit_from == 'kelvin':
        print(f"{temp} Kelvin is equivalent to:")
        print(f"{kelvin_to_celsius(temp)} Celsius")
        print(f"{kelvin_to_fahrenheit(temp)} Fahrenheit")
    else:
        print("Invalid unit. Please enter Celsius, Fahrenheit, or Kelvin.")

if __name__ == "__main__":
    main()
