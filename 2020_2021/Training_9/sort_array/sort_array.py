from lib.types import IStdin, IStdout
import random


def main(stdin: IStdin, stdout: IStdout):

    stdout.write("This time you will have to sort 100 arrays\n")

    for i in range(100):

        a = [random.randint(-200, 200) for _ in range(random.randint(10, 30))]

        stdout.write(f"Array {i + 1}: {' '.join(map(str, a))}\n")
        stdout.write("Answer >> ")
        stdout.flush()

        answer = stdin.readline().strip()

        if answer != " ".join(map(str, sorted(a))):
            stdout.write("Wrooong!\n")
            return

    stdout.write("Flag: donnuCTF{kinda_s0r71ng_sta710n}\n")
