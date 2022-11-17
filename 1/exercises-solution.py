data = [6, 8, 3, 5, 9, 10]

names = {"dog": "peanut", "cat": "willow", "lizard": "rodney",
	"giraffe": "rose", "whale": "whisper"}

# Exercise 1: Can you write a function that prints every other element of data:
# Correct output: 6, 3, 9
def ex1():
	L = len(data)
	for i in range(0, L, 2):
		print(data[i])

# Exercise 2: Write a function that prints the types of animals with 
# 	      names that start with "w"
# Correct output: "cat", "whale"
def ex2():
	for key in names.keys():
		val = names[key]
		if val[0] == "w":
			print(key)

# Final Exercise: Write a main() function which calls the other exercise functions and
#                 the final 2 lines to execute the function when the file is run
def main():
	ex1()
	ex2()

if __name__ == "__main__":
	main()
