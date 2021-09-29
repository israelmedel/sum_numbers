import csv

def numbers():

# open the file
    with open("sum_numbers.csv") as file:

# variables
        rows_number = 0
        columns_number = 0
        rows_list = {}
        counter = 0

# get rows and columns number, and fill the list for sum
        for row in csv.reader(file):
            rows_number += 1
            rows_list[counter] = row
            counter += 1
        for column in row:
            columns_number += 1

# iterate the list for sum
        for i in range(columns_number):
            total = 0
            for j in range(rows_number):
                total = total + int(rows_list[j][i])
            print('Column', i, '=', total)


numbers()
