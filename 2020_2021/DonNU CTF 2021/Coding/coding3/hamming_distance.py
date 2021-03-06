import random
from lib.types import IStdin, IStdout


def hamming_distance(a, b):
    counter = 0
    for i in str(bin(a ^ b)):
        if i == '1': counter += 1
    return counter


def main(stdin: IStdin, stdout: IStdout):

    stdout.write("To get the flag you will need to calculate the Hamming distance of two numbers 100 times.\n")
    stdout.write("Hamming distance is number of bits at which two numbers differ.\n")
    stdout.write("Example: for 3 (011) and 5 (101) Hamming distance equals 2\n")

    for i in range(100):

        x, y = random.randint(1, 2 ** 32), random.randint(1, 2 ** 32)
        stdout.write(f"Round {i + 1}: {x} {y}\n")
        stdout.write("Answer >> ")
        stdout.flush()
        try:
            answer = int(stdin.readline().strip())
            if answer != hamming_distance(x, y):
                stdout.write("Wrooong\n")
                return None
        except Exception:
            stdout.write("You must answer with a single number\n")
            return None

    stdout.write("Congratulations! Your flag is donnuCTF{x0r_15_th3_answer}\n")
