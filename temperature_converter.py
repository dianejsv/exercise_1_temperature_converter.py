# Ask the user to enter the temperature
temperature = float(input("Enter the temperature: "))

# Provide the available conversion type
print("\nChoose conversion type:")
print("Enter {C} " "for Fahrenheit to Celsius")
print("Enter {F} " "for Celsius to Fahrenheit")

# Prompt the user to select conversion type
conversion_type = (input("\nChoose the conversion type (C/F): ")).strip().upper()

# Conditional Statements
if conversion_type == "C":
    convert = (temperature - 32) * 5 / 9  # Formula to compute °F to °C
    print(f"Your converted temperature is {round(convert, 2)}°C")
elif conversion_type == "F":
    