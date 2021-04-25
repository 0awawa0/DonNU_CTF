import random
from lib.types import IStdin, IStdout


def largestSubArray(arr):
    currSum = arr[0]
    maxSum = arr[0]

    for i in range(1, len(arr)):
        currSum = max(arr[i], currSum + arr[i])
        maxSum = max(currSum, maxSum)

    return maxSum


def main(stdin: IStdin, stdout: IStdout):

    stdout.write("I will send you 100 arrays. For each array find the contiguous subarray (containing at least one number) which has the largest sum and sand back its sum\n")
    stdout.write("Example:\n")
    stdout.write("For array -2 1 -3 4 -1 2 1 -5 4 largest number is 6 (4 -1 2 1)\n")

    for i in range(100):
        array = [random.randint(-100, 100) for _ in range(random.randint(10, 40))]
        maxSum = largestSubArray(array)
        stdout.write(f"Array {i + 1}: {' '.join(str(j) for j in array)}\n")
        stdout.write("Answer >> ")
        stdout.flush()
        try:
            answer = int(stdin.readline().strip())
            if answer != maxSum:
                stdout.write("Wrong\n")
                return None
        except Exception:
            stdout.write("Error occurred. Send one number only\n")
            return None

    stdout.write("Congratulations! Your flag: donnuCTF{b2ec60d5c8d9618bc114e1c4c943894f}\n")
