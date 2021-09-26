import csv


FILE_PATH = "../data/students.csv"
SORTED_FILE_PATH = '../data/students_sorted.csv'


def get_students_data(file_path):
    data_list = [] 
    with open(file_path, 'r') as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            data_list.append(dict(row))
    
    return data_list


def store_students_data(file_path, data):
    with open(file_path, 'w', newline='') as file:
        field_names = list(data[0]) # ['student name', 'age', 'average mark']      
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def sort_students_by_age(file_path):
    students = get_students_data(file_path)   
    students_sorted_desc = sorted(students, key = lambda ele: ele['age'], reverse=True)  
    store_students_data(SORTED_FILE_PATH, students_sorted_desc)


sort_students_by_age(FILE_PATH)