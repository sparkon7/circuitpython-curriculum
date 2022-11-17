class MyCar:

	'''
	Missing #1) Add an argument to the constructor for the car's speed
	'''
	def __init__(self, name, ???):
		self.name = name
		???
		self.position = 0

	'''
	Missing #2) Use the cars speed and the steps (X) to update the position
	'''
	def move_forward(self, X):
		self.position = ???
		return self.position

	def report(self):
		message = "Car name: " + self.name
		message = message + ", "
		message = message + "Position: " + str(self.position)
		return message

'''
Missing #3) Write the logic in the main() function to create a car, move it, and report
'''
def main():
	???
	report = mycar.report()
	print(report)

if __name__ == "__main__":
	main()
