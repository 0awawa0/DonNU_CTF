from lib.types import IStdin, IStdout
import random


def main(stdin: IStdin, stdout: IStdout):

    stdout.write("This time you will have to sort an array\n")

    a = [random.randint(-200, 200) for _ in range(random.randint(10, 30))]

    stdout.write(f"Array: {' '.join(map(str, a))}\n")
    stdout.write("Answer >> ")
    stdout.flush()

    answer = stdin.readline().strip()

    if answer != " ".join(map(str, sorted(a))):
        stdout.write("Wrooong!\n")
        return

    stdout.write("Flag: donnuCTF{d1d_u_us3_th3_bubble_s0r7}\n")
