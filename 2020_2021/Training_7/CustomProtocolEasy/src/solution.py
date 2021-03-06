import Protocol
import json
from ezRSA.ezRSA import *


packets = json.load(open("packets.json"))

useful_packets = []
for packet in packets:
	if "tcp.payload" in packet["_source"]["layers"]["tcp"]:
		useful_packets.append(packet)


client_cipher_map = {}
for packet in useful_packets:
	client_port = packet["_source"]["layers"]["tcp"]["tcp.dstport"]
	data = packet["_source"]["layers"]["tcp"]["tcp.payload"].replace(":", "")
	if data[:8] == Protocol.PacketInterface.MAGIC_NUMBER_CONNECT_RESPONSE:
		primes = [int(i, 16) for i in int_to_bytes(int(data[8:], 16)).decode().split(":")]
		client_cipher_map[client_port] = RSA.fromPrimesOnly(primes)

messages = []
for packet in useful_packets:
	client_port = packet["_source"]["layers"]["tcp"]["tcp.srcport"]
	if client_port == "43584": continue

	data = packet["_source"]["layers"]["tcp"]["tcp.payload"].replace(":", "")
	if data[:8] == Protocol.PacketInterface.MAGIC_NUMBER_MESSAGE_REQUEST:
		message = int_to_bytes(int(data[8:], 16)).decode().split("::")
		nickname = message[0]
		text = int(message[1], 16)
		messages.append(nickname + "::" + int_to_bytes(client_cipher_map[client_port].decrypt(text)).decode())

for message in messages:
	print(message)
