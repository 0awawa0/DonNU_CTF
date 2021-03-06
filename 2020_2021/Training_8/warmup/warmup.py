from lib.types import IStdin, IStdout
import random


def main(stdin: IStdin, stdout: IStdout):
    stdout.write("I will send you a number N, you must answer with another number A such that:\n")
    stdout.write("""
      
     /N + 1, N mod 2 = 0
A = |
     \\N - 1, N mod 2 != 0


""")
    stdout.flush()
    stdout.write("Do that 1000 times. Let's go!\n\n")

    for i in range(1000):
        N = random.randint(2, 2**32)
        stdout.write(f"{N}\n")
        stdout.write(f">> ")
        stdout.flush()
        try:
            A = int(stdin.readline().strip())
            if N % 2:
                if A != N - 1:
                    stdout.write("Wrooong!\n")
                    return
            else:
                if A != N + 1:
                    stdout.write("Wrooong!\n")
                    return
        except Exception:
            return

    stdout.write("Good job, bye!\n")
