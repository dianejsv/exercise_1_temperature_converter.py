# Ask the user to enter the temperature
temperature = float(input("Enter the temperature: "))

# Provide the available conversion type
print("\nChoose conversion type:")
print("Enter {C} " "for Fahrenheit to Celsius")
print("Enter {F} " "for Celsius to Fahrenheit")

# Prompt the user to select conversion type
conversion_type = (input("\nChoose the conversion type (C/F): ")).strip().upper()