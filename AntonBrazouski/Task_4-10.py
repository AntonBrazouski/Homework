def generate_squares(num):
    return {i: i*i for i in range(1, num+1)}


num = 5
print(num)
print(generate_squares(num))