
FILE_READ = '../data/unsorted_names.txt'
FILE_WRITE = '../data/sorted_names.txt'

names = []

with open(FILE_READ, 'r') as f:
    names = f.readlines()

names.sort()

with open(FILE_WRITE, 'w') as f:
    for line in names:
        f.write(line)
