import json
import Protocol
from ezRSA.ezRSA import *


def common_modulus_attack(msg1, msg2, e1, e2, modulus):

	res = egcd(e1, e2)
	s1 = res['a']
	s2 = res['b']

	c1 = msg1
	if s1 < 0:
		c1 = egcd(c1, modulus)['a'] % modulus
		s1 = -s1

	c2 = msg2
	if s2 < 0:
		c2 = egcd(c2, modulus)['a'] % modulus
		s2 = -s2

	return (pow(c1, s1, modulus) * pow(c2, s2, modulus)) % modulus


packets = json.load(open("packets.json", 'r'))
modulus = int(open("./encryptionParams/modulus.txt", 'r').read())

filtered_packets = []
for packet in packets:
	if "tcp.payload" in packet["_source"]["layers"]["tcp"]:
		filtered_packets.append(packet["_source"]["layers"]["tcp"])

indexes = {}
for packet in filtered_packets:
	data = packet["tcp.payload"].replace(":", "")
	if data[:8] == Protocol.PacketInterface.MAGIC_NUMBER_CONNECT_RESPONSE:
		indexes[packet["tcp.dstport"]] = int(data[8:], 16)

nicknames = {}
for packet in filtered_packets:
	data = packet["tcp.payload"].replace(":", "")
	if data[:8] == Protocol.PacketInterface.MAGIC_NUMBER_NICKNAME_REQUEST:
		nicknames[packet["tcp.srcport"]] = int_to_bytes(int(data[8:], 16)).decode()

exponents = {}
e_array = [int(i) for i in open("./encryptionParams/e_array.txt", 'r').readlines()]

for index in indexes.keys():
	exponents[index] = e_array[indexes[index]]

messages = []
for packet in filtered_packets:
	data = packet["tcp.payload"].replace(":", "")
	if data[:8] == Protocol.PacketInterface.MAGIC_NUMBER_MESSAGE_REQUEST and packet["tcp.srcport"] == "43584":
		message = int_to_bytes(int(data[8:], 16)).decode()
		messages.append(packet)

tripplets = []

for i in range(0, len(messages), 3):
	tripplet = {messages[i]["tcp.dstport"]: messages[i]["tcp.payload"],
				messages[i + 1]["tcp.dstport"]: messages[i + 1]["tcp.payload"],
				messages[i + 2]["tcp.dstport"]: messages[i + 2]["tcp.payload"]}
	tripplets.append(tripplet)

port1 = '52143'
port2 = '52144'

for tripplet in tripplets:
	msg1 = tripplet[port1]
	msg2 = tripplet[port2]

	msg1 = int(int_to_bytes(int(msg1.replace(":", "")[8:], 16)).decode().split("::")[1], 16)
	msg2 = int(int_to_bytes(int(msg2.replace(":", "")[8:], 16)).decode().split("::")[1], 16)

	print(int_to_bytes(common_modulus_attack(msg1, msg2, exponents[port1], exponents[port2], modulus)))
