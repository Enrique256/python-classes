"""
4. In this assignment, you will use python’s built-in string methods to interact with the string.

sentence=“Python is my favorite programming language!”
Write a program called string_methods.py in which you define the string above. After defining it, you will use string methods to perform the next tasks.
Print the full string as it is.
Print a version of the string with only uppercase letters.
Print the number of times letter “o” is present in the string.
Print a version of the string in which “my” is replaced with “everyone’s”

"""
sentence="Python is my favorite programming language!"
print(sentence)
print("Uppercase string:", sentence.upper())
print("No. of 'o's in the string:",sentence.count("o"))
print("reaplaced strings:", sentence.replace("my","everyone's"))