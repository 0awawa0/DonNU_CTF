import random
from lib.types import IStdin, IStdout


def generate_array():
    is_mountain = random.getrandbits(1)
    result = [random.randint(0, 1200) for _ in range(random.randint(3, 100))]

    if is_mountain:
        result = []
        size = random.randint(3, 100)
        peak_index = random.randint(0, size - 2)
        max_step = random.randint(2, 100)
        next_num = random.randint(1, 100)

        for i in range(peak_index + 1):
            result.append(next_num)
            next_num = random.randint(next_num + 1, next_num + max_step)

        for i in range(peak_index + 1, -1, -1):
            next_num = random.randint(next_num - max_step, next_num - 1)
            result.append(next_num)

    return result, check_is_mountain(result)


def check_is_mountain(arr):
    if len(arr) < 3: return False
    if arr[0] > arr[1]: return False

    rising = True
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]: return False
        if arr[i] < arr[i + 1] and not rising: return False
        if arr[i] > arr[i + 1] and rising: rising = False

    return True and not rising


def main(stdin: IStdin, stdout: IStdout):

    stdout.write("I will send you 100 arrays. For each array check if the array is a mountain array and return 1 if it is a mountain or 0 otherwise\n")
    stdout.write("Array is a mountain array if there is an index i (peak of the array) such that:\n")
    stdout.write("\t- for any j < i array[j] < array[j + 1]\n")
    stdout.write("\t- for any k > i array[k] < array[k - 1]\n")

    for i in range(100):
        array, is_mountain = generate_array()
        stdout.write(f"Array {i + 1}: {' '.join(str(j) for j in array)}\n")
        stdout.write("Answer >> ")
        stdout.flush()
        try:
            answer = int(stdin.readline().strip())
            if (answer and not is_mountain) or (not answer and is_mountain):
                stdout.write("Wroong\n")
                return None
        except Exception:
            stdout.write("Error occurred.Send only 1 or 0 as an answer\n")
            return None

    stdout.write("Congratulations! Your flag: donnuCTF{reached_th3_peak}\n")
