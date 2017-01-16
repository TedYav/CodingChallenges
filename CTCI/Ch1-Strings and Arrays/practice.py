#  bla bla I get it

class ArrayList:
	def __init__(self, length=16):
		self._arr = [None] * length

	def get(self, i):
		self.__validate(i)
		return self._arr[i]

	def set(self, i, value):

		self._arr[i] = value

	def append(self, ele):

	def __validate(self, i):
		if i >= len(self._arr) or i < 0:
			raise IndexError()


class StringBuilder:
	def __init__(self, str):
