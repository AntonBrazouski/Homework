import csv

FILE_PATH = "../data/students.csv"


def get_students_data(file_path):
    data_list = [] 
    with open(file_path, 'r') as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            data_list.append(dict(row))
    
    return data_list


def get_top_performers(file_path, number_of_top_students=5):
    students = get_students_data(file_path)   
    students_sorted = sorted(students, key = lambda ele: ele['average mark'], reverse=True)  
    top_students = students_sorted[:number_of_top_students]
    top_names = [student['student name'] for student in top_students]

    return top_names


print(get_top_performers(FILE_PATH))

