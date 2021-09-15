# ### Task 1.6
# Write a program which makes a pretty print of a part of the multiplication table.
# Examples:
# ```
# Input:
# a = 2
# b = 4
# c = 3
# d = 7

# Output:
# 	3	4	5	6	7	
# 2	6	8	10	12	14	
# 3	9	12	15	18	21	
# 4	12	16	20	24	28
# ```


def multi_with_pretty(cords=(2, 4, 3, 7)):
    line = ''

    # headline
    for x in range(cords[2], cords[3]+1):
        line += (str(x) + '\t')
    print('\t'+ line)

    # sideline and data
    for y in range(cords[0], cords[1]+1):
        line = (str(y) + '\t')
        for x in range(cords[2], cords[3]+1):
            line += (str(x*y) + '\t')
        print(line)
        line = ''
            

multi_with_pretty()
