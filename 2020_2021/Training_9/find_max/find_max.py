from lib.types import IStdin, IStdout
import random


def main(stdin: IStdin, stdout: IStdout):

    stdout.write("Find max in the arrays I will send you and send it back to me. There will be 100 arrays\n")

    for i in range(100):
        a = [random.randint(-100, 100) for _ in range(random.randint(10, 40))]
        stdout.write(f"Array {i + 1}: {' '.join(map(str, a))}\n")
        stdout.write("Answer >> ")
        stdout.flush()
        try:
            answer = int(stdin.readline().strip())
            if answer != max(a):
                stdout.write("Wrooong.\n")
                return
        except Exception:
            stdout.write("Wrong input!\n")
            return

    stdout.write("Good job. Flag: donnuCTF{ha_c1assic}\n")
