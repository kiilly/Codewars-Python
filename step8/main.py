def solution(n):
    roman = ''  #intitiate an empty string
    while n >= 1000: n = n - 1000 ; roman = roman + "M"
    while n >= 900: n = n - 900 ; roman = roman + "CM"
    while n >= 500: n = n - 500 ; roman = roman + "D"
    while n >= 400: n = n - 400 ; roman = roman + "CD"
    while n >= 100: n = n - 100 ; roman = roman + "C"
    while n >= 90: n = n - 90 ; roman = roman + "XC"
    while n >= 50: n = n - 50 ; roman = roman + "L"
    while n >= 40: n = n - 40 ; roman = roman + "XL"
    while n >= 10: n = n - 10 ; roman = roman + "X"
    while n >= 9: n = n - 9 ; roman = roman + "IX"
    while n >= 5: n = n - 5 ; roman = roman + "V"
    while n >= 4: n = n - 4 ; roman = roman + "IV"
    while n >= 1: n = n - 1 ; roman = roman + "I"
    return roman

# for each letter a number is associated
# each time a number is detected it is subtracted to the initial number
# and its associated letter is written in the roman string
