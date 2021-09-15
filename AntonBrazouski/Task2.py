
# ## Task 1.2
# Write a Python program to count the number of characters (character frequency) in a string (ignore case of letters).
# Examples:
# ```
# Input: 'Oh, it is python' 
# Output: {',': 1, ' ': 3, 'o': 2, 'h': 2, 'i': 2, 't': 2, 's': 1, 'p': 1, 'y': 1, 'n': 1}
# ```



astring = 'just_another_string'

def frequency_calculator(astring):
    astring = astring.lower()
    characters_data = {}

    for ch in astring:
        characters_data[ch] = characters_data.get(ch, 0) + 1 

    return characters_data

print(frequency_calculator(astring))