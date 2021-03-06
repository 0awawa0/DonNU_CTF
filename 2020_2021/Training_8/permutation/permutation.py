import random
from lib.types import IStdin, IStdout


def shift_rows(s):
    s[1][0], s[1][1], s[1][2], s[1][3] = s[1][1], s[1][2], s[1][3], s[1][0]
    s[2][0], s[2][1], s[2][2], s[2][3] = s[2][2], s[2][3], s[2][0], s[2][1]
    s[3][0], s[3][1], s[3][2], s[3][3] = s[3][3], s[3][0], s[3][1], s[3][2]
    return s


def inv_shift_rows(s):
    s[1][0], s[1][1], s[1][2], s[1][3] = s[1][3], s[1][0], s[1][1], s[1][2]
    s[2][0], s[2][1], s[2][2], s[2][3] = s[2][2], s[2][3], s[2][0], s[2][1]
    s[3][0], s[3][1], s[3][2], s[3][3] = s[3][1], s[3][2], s[3][3], s[3][0]
    return s


def main(stdin: IStdin, stdout: IStdout):

    stdout.write("To get the flag you need to perform shift or inverse shift to the given 100 4x4 matrices\n")
    stdout.write("First line is operation to perform: 1 - to shift forward, 2 - to inverse shift\n")
    stdout.write("Next four lines will be the matrix\n")
    stdout.write("Send answers as a 1x16 vectors\n")
    stdout.write("Let's go!\n")

    for k in range(100):
        stdout.write(f"Round {k + 1}:\n")

        operation = random.randint(1, 2)
        stdout.write(f"{operation}\n")

        matrix = []
        for i in range(4):
            matrix.append([random.randint(0, 100) for _ in range(4)])
            stdout.write(f"{matrix[i][0]} {matrix[i][1]} {matrix[i][2]} {matrix[i][3]}\n")

        if operation == 1:
            matrix = shift_rows(matrix)
        elif operation == 2:
            matrix = inv_shift_rows(matrix)

        try:
            stdout.write("Your array >> ")
            stdout.flush()

            line = stdin.readline().strip()

            right_answer = ""
            for i in range(4):
                right_answer += " ".join([str(i) for i in matrix[i]]) + " "
            if line == right_answer.strip():
                stdout.write("Right\n")
            else:
                print(right_answer)
                stdout.write("Wrooong. That's another array\n")
                return
        except Exception as exception:
            print(exception)
            stdout.write("Wrooong. That doesn't look like numbers -_-\n")
            return

    stdout.write("Well done! Here's your flag:" + open("src/ctf_tasks/permutation/flag.txt", 'r').read())