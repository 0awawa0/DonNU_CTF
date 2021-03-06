import random
from lib.types import IStdin, IStdout


def main(stdin: IStdin, stdout: IStdout):
    stdout.write("Welcome to a classic 'Bulls and Cows' game. You can find rules here: https://ru.wikipedia.org/wiki/Быки_и_коровы\n")
    stdout.write("To get the flag you have to guess the number in 7 tries or less. Good luck\n")

    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    number = ""
    for i in range(4):
        d = random.choice(digits)
        digits.remove(d)
        number += d

    t = 1
    while True:
        stdout.write(f"Try {t} >> ")
        stdout.flush()
        answer = stdin.readline().strip()
        if len(set(answer)) != len(answer) or len(answer) != 4:
            stdout.write("You are doing it wrong!\n")
            t += 1
        else:
            if answer == number:
                stdout.write("Yes! That is a number. Your flag: " + open("./src/ctf_tasks/bulls_and_cows/flag.txt").read() + '\n')
                return

            bulls = 0
            cows = 0
            for k in answer:
                if k in number:
                    if number.index(k) == answer.index(k):
                        bulls += 1
                    else:
                        cows += 1
            stdout.write(f"Bulls: {bulls} Cows: {cows}\n")
            t += 1
        if t > 7:
            stdout.write("You're out of tries. See ya.\n")
            return
