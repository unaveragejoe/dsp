import pprint as pp
def count_degrees(csv_file_name):
    file = open(csv_file_name, 'r').readlines()
    file_list = file.split('\n')

    pp.pprint(file)

count_degrees('faculty.csv')