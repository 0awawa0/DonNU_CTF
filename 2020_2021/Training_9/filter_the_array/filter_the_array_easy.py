from lib.types import IStdin, IStdout
import random


def apply_filters(a):
    res = []

    for i in range(len(a)):
        if a[i] == 0:
            res.append(a[i])

        if not a[i] % 5:
            continue

        if a[i] % 2 and i % 2:
            continue

        if not (a[i] % 2) and not (i % 2):
            continue

        res.append(a[i])

    return res


def main(stdin: IStdin, stdout: IStdout):

    stdout.write("For given array apply the following filters:\n")
    stdout.write(" - never delete 0\n")
    stdout.write(" - delete number if it is multiple by 5\n")
    stdout.write(" - delete number if it is even and is on even position\n")
    stdout.write(" - delete number if it is odd and is on odd position\n")

    a = [random.randint(0, 1000) for _ in range(random.randint(10, 100))]
    a.append(0)

    random.shuffle(a)

    stdout.write(f"Array: {' '.join(map(str, a))}\n")
    stdout.write("Answer >> ")
    stdout.flush()

    filtered = apply_filters(a)
    try:
        answer = list(map(int, stdin.readline().strip().split(" ")))

        if filtered != answer:
            stdout.write(f"Wroong! It was: {filtered}\n")
            return

    except Exception:
        stdout.write("Wrong input.\n")
        return

    stdout.write("Good job! Flag: donnuCTF{jus7_r3m0v3_som37thing}\n")
