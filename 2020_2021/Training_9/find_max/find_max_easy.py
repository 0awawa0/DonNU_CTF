from lib.types import IStdin, IStdout
import random


def main(stdin: IStdin, stdout: IStdout):

    stdout.write("Find max in the array I will send you and send it back to me\n")

    a = [random.randint(-100, 100) for _ in range(random.randint(10, 40))]
    stdout.write(f"Array: {' '.join(map(str, a))}\n")
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

    stdout.write("Good job. Flag: donnuCTF{lin3ar_s3arch_it_is}\n")
