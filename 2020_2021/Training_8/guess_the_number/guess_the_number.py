import random
from lib.types import IStdin, IStdout


def main(stdin: IStdin, stdout: IStdout):
    stdout.write("I am thinking of the number in range 1 - 100. Can you guess it in 7 or less tries?\n")

    counter = 7
    c = 1

    n = random.randint(1, 100)
    while True:
        stdout.write(f"Try {c} >> ")
        stdout.flush()
        t = int(stdin.readline().strip())
        if t == n:
            stdout.write("Yeah, that's the number! Your flag: " + open("./src/ctf_tasks/guess_the_number/flag.txt", 'r').read() + "\n")
            return
        else:
            if t < n:
                stdout.write("Higher\n")
            else:
                stdout.write("Less\n")

        counter -= 1
        c += 1

        if counter == 0:
            stdout.write("You are out of tries. Good luck next time\n")
