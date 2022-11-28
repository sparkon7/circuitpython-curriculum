# The purpose of the `Adder` class is to store a list of numbers,
# allow a user to append more numbers to the list, and then
# provide a method to add the numbers in the list together 
# and return the value

# create a class named `Adder`
class Adder:

	# write the initializer method with one argument
	#    numbers: the initial list of numbers
	#
	# the initializer should set two class properties,
	#    nums: the list of numbers to add together
	#    result: the result of the addition. This starts at 0
	def __init__(self, numbers):
		self.nums = numbers
		self.result = 0

	# write the method `append_number`, with one argument
	#    n: the number to append to `self.nums`
	def add_number(self, n):
		self.nums.append(n)

	# write the `compute` method, which takes no arguments.
	# loop through `self.nums`, adding each value to `self.result`
	# return the result
	def compute(self):
		for n in self.nums:
			self.result += n
		return self.result

# write the `main` function to do the following:
# - create an `Adder` instance with the following initial `numbers`: [1, 3, 5]
# - use the `add_number` function to add the number 7 to our list
# - call the `compute` function and store the output in a variable named `res`
# - print `res` to the console
def main():
	myadd = Adder([1, 3, 5])
	myadd.add_number(7)
	res = myadd.compute()
	print(res)
	

# include the code that will call the `main` function when this script is run
if __name__ == "__main__":
	main()
