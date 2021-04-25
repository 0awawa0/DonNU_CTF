from lib.types import IStdin, IStdout
import random


def generate_equation():
    a = random.randint(1, 1000)
    b = random.randint(1, 1000)
    c = random.randint(1, 1000)
    while b * b <= 4 * a * c:
        a = random.randint(1, 1000)
        b = random.randint(1, 1000)
        c = random.randint(1, 1000)

    x1 = (-b + (b * b - 4 * a * c) ** 0.5) / (2 * a)
    x2 = (-b - (b * b - 4 * a * c) ** 0.5) / (2 * a)
    return a, b, c, x1, x2


def main(stdin: IStdin, stdout: IStdout):

    stdout.write("Hi, in this task you need to solve quadratic equation to get the flag\n")
    stdout.write("I will send coefficients as three numbers and you should send the answer back\n")
    stdout.write("Example: 2, 5, 2 is for equation 2 * x^2 + 5 * x + 2 = 0\n")
    stdout.write("And the answer will be: -2 -0.5. Round answer to two decimal places stripping zeros\n")

    a, b, c, x1, x2 = generate_equation()
    stdout.write(f"Equation: {a}, {b}, {c}\n")
    stdout.write(f"Answer >> ")
    stdout.flush()

    try:
        a1, a2 = tuple(map(float, stdin.readline().strip().split(" ")))

        if str(round(a1, 2)) != str(round(x1, 2)) and str(round(a1, 2)) != str(round(x2, 2)):
            stdout.write("Wrooong.\n")
            return

        if str(round(a2, 2)) != str(round(x1, 2)) and str(round(a2, 2)) != str(round(x2, 2)):
            stdout.write("Wrooong.\n")
            return
    except Exception:
        stdout.write("Wrong input!\n")
        return

    stdout.write("Congratulations. Your flag is: donnuCTF{thank_g0d_discriminant_is_n0t_negativ3}\n")
