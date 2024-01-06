
#3 Temperature Converter
def celsius_to_fahrenheit(cel):
    fahr=cel*(9/5)+32
    return fahr
cel=int(input("Enter a temperature in degree celsius: "))
r=celsius_to_fahrenheit(cel)
print(f"{cel} degree celsius is equal to {r} fahreheit.")
