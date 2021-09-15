# ### Task 1.3
# Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form.
#Examples:
# ```
# Input: ['red', 'white', 'black', 'red', 'green', 'black']
# Output: ['black', 'green', 'red', 'white', 'red']
# ```

fruits = ['apple', 'apple', 'banana', 'cherry', 'pineapple', 'cherry']

result = sorted(set(fruits))

print(result)