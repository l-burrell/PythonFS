def calcAge(current_year=2021):
    birth_year = int(input('What is the year you were born? '))
    return current_year - birth_year

print(calcAge())