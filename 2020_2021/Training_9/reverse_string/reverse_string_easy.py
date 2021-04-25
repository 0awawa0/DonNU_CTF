from lib.types import IStdin, IStdout
import string
import random


alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits


def main(stdin: IStdin, stdout: IStdout):

    stdout.write("I will send you a string and you must reverse it and send back to me to get the flag\n")

    s = "".join([random.choice(alphabet) for _ in range(random.randint(10, 100))])
    stdout.write(f"String: {s}\n")
    stdout.write(f"Answer >> ")
    stdout.flush()

    answer = stdin.readline().strip()

    if answer != "".join(reversed(s)):
        stdout.write("Wroong!\n")
        return

    stdout.write("Nice! Flag: donnuCTF{unr3adable_3ith3r_way}\n")
