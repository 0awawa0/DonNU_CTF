def roman_to_int(s):
    number = 0
    prevChar = '_'

    for i in range(len(s) - 1, -1, -1):
        if s[i] == 'I':
            if prevChar in "VX":
                number += -1
            else:
                number += 1
        elif s[i] == 'V':
            number += 5
        elif s[i] == 'X':
            if prevChar in "LC":
                number += -10
            else:
                number += 10
        elif s[i] == 'L':
            number += 50
        elif s[i] == 'C':
            if prevChar in "DM":
                number += -100
            else:
                number += 100
        elif s[i] == 'D':
            number += 500
        elif s[i] == 'M':
            number += 1000
        else:
            number += 0
        prevChar = s[i]

    return number


def int_to_roman(number):

    nums = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]

    result = ""
    number = number

    for n in nums:
        while number >= n[0]:
            number -= n[0]
            result += n[1]

    return result

for i in range(1, 4000):
    assert(roman_to_int(int_to_roman(i)) == i)

print("Test passed")