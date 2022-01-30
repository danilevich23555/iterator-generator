nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

class FlatIterator:
	def __init__(self, list1):
		self.list1 = list1

	def __iter__(self):
		self.cursor = 0
		self.cursor1 = -1
		self.my_list_row = self.list1
		return self

	def __next__(self):
		if self.cursor1 < len(self.my_list_row[self.cursor]) -1:
			self.cursor1 += 1
		elif self.cursor1 == len(self.my_list_row[self.cursor])-1 and self.cursor < len(self.list1)-1:
			self.cursor1 = 0
			self.cursor += 1
		else:
			raise StopIteration
		return self.my_list_row[self.cursor][self.cursor1]


for item in FlatIterator(nested_list):
	print(item) #
