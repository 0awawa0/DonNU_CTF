import random
from lib.types import IStdin, IStdout


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


def main(stdin: IStdin, stdout: IStdout):

    stdout.write("I will send you 1000 roman numbers. To get the flag convert each of it to decimal and send back\n")
    stdout.write("Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.\n")
    stdout.write("I - 1, V - 5, X - 10, L - 50, C - 100, D - 500, M - 1000\n")
    stdout.write("For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.\n")
    stdout.write("Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:\n")
    stdout.write("\t- I can be placed before V and X to make 4 and 9\n")
    stdout.write("\t- X can be placed before L and C to make 40 and 90\n")
    stdout.write("\t- C can be placed before D and M to make 400 and 900\n")

    for i in range(1000):
        number = random.randint(1, 3999)
        roman = int_to_roman(number)
        stdout.write(f"Number {i + 1}: {roman}\n")
        stdout.write("Answer >> ")
        stdout.flush()
        try:
            answer = int(stdin.readline().strip())
            if answer != number:
                stdout.write("Wrong\n")
                return None
        except Exception:
            stdout.write("Error occurred. Send one number only\n")
            return None

    stdout.write("Congratulations! Your flag: donnuCTF{364e0898e04eb0fd0f97a0381ff50aed}\n")
