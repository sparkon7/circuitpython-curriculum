class Car:
	def __init__(self, name):
		self.name = name
		self.position = 0

	def move_forward(self, X):
		self.position = self.position + X
		return self.position

	def report(self):
		message = "Car name: " + self.name
		message = message + ", "
		message = message + "Position: " + str(self.position)
		return message

def main():
	mycar = Car("subaru")
	mycar.move_forward(10)
	mycar.move_forward(-3)
	report = mycar.report()
	print(report)

if __name__ == "__main__":
	main()
