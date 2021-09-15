# ### Task 1.6
# Write a Python program to convert a given tuple of positive integers into an integer. 
# Examples:
# ```
# Input: (1, 2, 3, 4)
# Output: 1234
# ```

atuple = (1, 3, 4, 2)


result = 0
# for idx in range(len(atuple), 0, -1):
#     order = 10**(idx - 1)
#     result += atuple[-idx]* order

tuple_len = len(atuple)
for idx in range(tuple_len):
    order = 10**(tuple_len-idx-1)
    result += atuple[idx]*order



print(f"{atuple} \t {type(atuple)}")    
print(f"{result} \t\t {type(result)} ")