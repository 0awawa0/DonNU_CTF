import random
from lib.types import IStdin, IStdout


def main(stdin: IStdin, stdout: IStdout):

    stdout.write("To get the flag you need to convert 100 4x4 matrices into 1x16 vector\n")
    stdout.write("Let's go!\n")

    for _ in range(100):
        matrix = [random.randint(0, 100) for i in range(16)]

        for i in range(0, 16, 4):
            stdout.write(f"{matrix[i]} {matrix[i + 1]} {matrix[i + 2]} {matrix[i + 3]}\n")
        try:
            stdout.write("Your array >> ")
            stdout.flush()

            line = stdin.readline().strip()
            array = [int(i) for i in line.split(" ")]
            if array == matrix:
                stdout.write("Right\n")
            else:
                stdout.write("Wrooong. That's another array\n")
                return
        except Exception as exception:
            print(exception)
            stdout.write("Wrooong. That doesn't look like numbers -_-\n")
            return

    stdout.write("Well done! Here's your flag:" + open("src/ctf_tasks/matrix2bytes/flag.txt", 'r').read())
