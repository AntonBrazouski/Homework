### Task 1.4
# Write a Python program to sort a dictionary by key.


sample_dict = {'x': 7, 'a': 0, 'c': 200}
answer = {item : sample_dict[item] for item in sorted(sample_dict)}

print(sample_dict)
print(answer)
