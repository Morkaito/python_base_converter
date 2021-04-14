import argparse
import sys

def ret_hex_digit(num, bh=False, ret_values=False):
	num = str(num)
	hexKeys = ''
	hex_values = {"A":10, "B":11, "C":12, "D":13, "E":14, "F":15}
	hex_values_bits = {"0":"0000", "1":"0001", "2":"0010", "3":"0011", "4":"0100", "5":"0101", "6":"0110", "7":"0111",
	"8":"1000", "9":"1001", "A":"1010", "B":"1011", "C":"1100", "D":"1101", "E":"1110", "F":"1111"}
	if not bh:
		if num in hex_values.keys():
			return hex_values[num]
		else:
			return num
	elif bh:
		num = int(num)
		if num in hex_values.values():
			for key in hex_values.keys():
				if hex_values[key] == num:
					return str(key)
		else:
			return str(num)
	elif ret_values:
		if num in hex_values_bits.values():
			for key in hex_values_bits.keys():
				if hex_values_bits[key] == num:
					hexKeys += key
		return hexKeys
	else:
		if num in hex_values_bits.keys():
			return hex_values_bits[num]

def ret_octal_digit(num, op=False):
	num = str(num)
	octalKeys = ''
	octal_values_bits = {"0":"000", "1":"001", "2":"010", "3":"011", "4":"100", "5":"101", "6":"110", "7":"111" }
	if not op:
		if num in octal_values_bits.keys():
			return octal_values_bits[num]
	else:
		if num in octal_values_bits.values():
			for key in octal_values_bits.keys():
				if octal_values_bits[key] == num:
					octalKeys += key
		return octalKeys


def convert_dec(num, base):
	count = len(num) - 1
	result = 0
	if base == 16:
		for n in num:
			n = int(ret_hex_digit(n))
			result += n*(base**count)
			count -= 1
			return result
	else:
		for n in num:
			n = int(n)
			result += n*(base**count)
			count -= 1
		return result


def convert_hex(num, base):
	result = []
	bin_seq = []
	if base == 2:
		for n in num:
			bin_seq.append(n)
			if len(bin_seq) == 4:
				nseq = "".join(bin_seq)
				result.append(ret_hex_digit(nseq, bh=True, ret_values=1))
				bin_seq = []
		return "".join(result)
	elif base == 8:
		size_num = len(num) * 4
		result_hex = []
		for n in num:
			result.append(ret_octal_digit(n, op=False))
		result = "".join(result)
		while len(result) != size_num:
			result = list(result)
			result.insert(0, '0')
		for n in result:
			bin_seq.append(n)
			if len(bin_seq) == 4:
				nseq = "".join(bin_seq)
				result_hex.append(ret_hex_digit(nseq, bh=True))
				bin_seq = []
		return "".join(result_hex)
	else:
		while True:
			num = int(num)
			calc = num % 16
			num = num/16
			if num%16 == 0:
				break
			result.append(ret_hex_digit(calc, bh=True))
		result.reverse()
		return "".join(result)

		

def convert_octal(num, base):
	num = str(num)
	result = []
	bin_seq = []
	if base == 2:
		for n in num:
			bin_seq.append(n)
			if len(bin_seq) == 3:
				nseq = "".join(bin_seq)
				result.append(ret_octal_digit(nseq, op=True))
				bin_seq = []
		return "".join(result)

	elif base == 16:
		result_octal = []
		for n in num:
			result.append(ret_hex_digit(n, bh=True))
		result = "".join(result)
		for n in result:
			bin_seq.append(n)
			if len(bin_seq) == 3:
				nseq = "".join(bin_seq)
				result_octal.append(ret_octal_digit(nseq, op=True))
				bin_seq = []
		return "".join(result_octal)
	
	else:
		while True:
			num = int(num)
			calc = num % 8
			num = num/8
			if num == 0:
				break
			result.append(str(calc))
		if not result:
			sys.exit()
		else:
			result.reverse()
			return "".join(result)


def convert_bin(num, base):
	result = []
	if base == 16:
		for n in num:
			result.append(ret_hex_digit(n, bh=True))
		return "".join(result)
	elif base == 8:
		for n in num:
			result.append(ret_octal_digit(n))
		return "".join(result)
	else:
		#calc = 0
		while True:
			num = int(num)
			calc = num % 2
			num = num/2
			if calc != 0 and calc != 1:
				break
			elif num == 0:
				break
			result.append(str(calc))
		if not result:
			sys.exit()
		else:
			result.reverse()
			return "".join(result)


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Convert numerics base')
	parser.add_argument('num', help='numero', type=str)
	parser.add_argument('old_base', help='base numerica antiga', type=int)
	parser.add_argument('new_base', help='base numerica nova', type=int)
	args = parser.parse_args()
	if args.old_base == args.new_base:
		print('[!] - Bases numerica iguais')
		sys.exit()
	elif args.new_base == 10:
		print(convert_dec(args.num, args.old_base))
	elif args.new_base == 2:
		print(convert_bin(args.num, args.old_base))
	elif args.new_base == 8:
		print(convert_octal(args.num, args.old_base))
	else:
		print(convert_hex(args.num, args.old_base))


