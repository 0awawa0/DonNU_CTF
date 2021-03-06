import random
from string import ascii_lowercase
from lib.types import IStdin, IStdout


def main(stdin: IStdin, stdout: IStdout):
    stdout.write("Just repeat after me. You will figure it out. Secret is one word. Wrap it in donnuCTF{}\n")

    secret = "".join([f"{bin(ord(i))[2:]:0>8s}" for i in "penguins"])
    index = 0
    print(secret)
    while True:
        if secret[index] == '0':
            word = ""
            for i in range(4):
                word += random.choice(ascii_lowercase)
            stdout.write(word + "\n")
            answer = stdin.readline().strip()
            if word != answer:
                stdout.write("Wrong!\n")
                return
        else:
            word = ""
            for i in range(5):
                word += random.choice(ascii_lowercase)
            stdout.write(word + "\n")
            answer = stdin.readline().strip()
            if word != answer:
                stdout.write("Wrong!\n")
                return
        index = (index + 1) % len(secret)
