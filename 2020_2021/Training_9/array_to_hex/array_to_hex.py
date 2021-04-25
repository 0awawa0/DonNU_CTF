from lib.types import IStdin, IStdout
import random


def main(stdin: IStdin, stdout: IStdout):

    stdout.write("In this task you will need to convert given array into a single hex string 100 times\n")

    for i in range(100):

        a = [random.randint(0, 255) for _ in range(random.randint(10, 100))]

        stdout.write(f"Array {i + 1}: {' '.join(map(str, a))}\n")
        stdout.write("Answer >> ")
        stdout.flush()

        answer = stdin.readline().strip()

        if answer != "".join([hex(j)[2:] for j in a]):
            stdout.write("Wrong!\n")
            return

    stdout.write("Flag: donnuCTF{just_h3xlify}\n")
