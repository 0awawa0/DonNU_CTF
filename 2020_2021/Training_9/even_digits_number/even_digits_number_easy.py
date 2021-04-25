from lib.types import IStdin, IStdout
import random


def main(stdin: IStdin, stdout: IStdout):

    stdout.write("I will send you an array of positive numbers, you should send back count of numbers in the array with even number of digits in them.\n")

    count = 0
    a = [random.randint(2 ** 2, 2 ** 64) for _ in range(random.randint(10, 50))]

    for c in a:
        if not (len(str(c)) % 2):
            count += 1

    stdout.write(f"Array: {' '.join(list(map(str, a)))}\n")
    stdout.write("Answer >> ")
    stdout.flush()

    answer = stdin.readline().strip()

    if answer != str(count):
        stdout.write("Wrooong!\n")
        return

    stdout.write("Good job! Flag: donnuCTF{so_y0u_can_count}\n")
