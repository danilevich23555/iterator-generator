nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]



def flat_generator(nested_list):
	for str in nested_list:
		print(len(str))
		for element in str:
				yield element

for item in  flat_generator(nested_list):
	print(item)