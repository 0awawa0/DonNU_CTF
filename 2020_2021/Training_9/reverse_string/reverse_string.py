from lib.types import IStdin, IStdout
import string
import random


alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits


def main(stdin: IStdin, stdout: IStdout):

    stdout.write("I will send you 100 strings and you must reverse them and send back to me to get the flag\n")

    for i in range(100):

        s = "".join([random.choice(alphabet) for _ in range(random.randint(10, 100))])
        stdout.write(f"String {i + 1}: {s}\n")
        stdout.write(f"Answer >> ")
        stdout.flush()

        answer = stdin.readline().strip()

        if answer != "".join(reversed(s)):
            stdout.write("Wroong!\n")
            return

    stdout.write("Nice! Flag: donnuCTF{r3v3rsa1_1s_wha7_i_d0}\n")
