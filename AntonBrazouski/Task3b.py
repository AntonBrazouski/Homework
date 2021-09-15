# ### Task 1.3 
# Create a program that asks the user for a number and then prints out a list of all the [divisors](https://en.wikipedia.org/wiki/Divisor) of that number.
# Examples:
# ```
# Input: 60
# Output: {1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60}
# ```


def all_div(number):
    l = []
    user = ''
    
    while user != 'q':
        user = input("Please enter a number, or 'q' for exit: ")
        if user == 'q':
            return 'exit'
        else:
            try:
                number = int(user)
            except(ValueError):
                return 'Not an integer'    

            for i in range(1, number+1):
                if number % i == 0:
                    l.append(i)
            
            return l

print(all_div(100))
