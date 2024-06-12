def convert_to_roman(num):
    if not 1 <= num <= 3999:
        return "Invalid input. Please enter a number between 1 and 3999."

    roman_numerals = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    result = ''
    for value, numeral in roman_numerals.items():
        count = num // value
        result += numeral * count
        num -= value * count

    return result

# Example usage:
year = int(input("Enter a year (between 1 and 3999): "))
print(f"The Roman numeral representation of {year} is: {convert_to_roman(year)}")