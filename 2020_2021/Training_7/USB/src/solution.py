import json


KEY_MAP = {
	"a": "04",
	"b": "05",
	"c": "06",
	"d": "07",
	"e": "08",
	"f": "09",
	"g": "0a",
	"h": "0b",
	"i": "0c",
	"j": "0d",
	"k": "0e",
	"l": "0f",
	"m": "10",
	"n": "11",
	"o": "12",
	"p": "13",
	"q": "14",
	"r": "15",
	"s": "16",
	"t": "17",
	"u": "18",
	"v": "19",
	"w": "1a",
	"x": "1b",
	"y": "1c",
	"z": "1d",
	"1": "1e",
	"2": "1f",
	"3": "20",
	"4": "21",
	"5": "22",
	"6": "23",
	"7": "24",
	"8": "25",
	"9": "26",
	"0": "27",
	"\n": "28",
	" ": "2c",
	"_": "2d",
	"{": "2f",
	"}": "30"
}


dump = json.load(open('packets.json'))
flag = ""
for i in range(0, len(dump)):
	data = dump[i]["_source"]["layers"]["usb.capdata"].split(':')
	
	if data[2] == "00": continue

	for k in KEY_MAP:
		if KEY_MAP[k] == data[2]:
			if data[0] == "02":
				flag += k.upper()
			else:
				flag += k

print(flag)
