
input_data = open("output", 'rb').read()
input_data = input_data[0x2c:]

flag = ""
for i in range(0, len(input_data), 2):
    flag += str(1 - input_data[i + 1] & 0x1)
    flag += str(1 - input_data[i] & 0x1)

print(bytes.fromhex(hex(int(flag[:216], 2))[2:]))