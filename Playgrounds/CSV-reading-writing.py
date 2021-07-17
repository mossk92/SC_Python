import csv

#Q1
with open("CSV-starter/colours_20_simple.csv") as csv_file:
    csv_reader = csv.reader(csv_file,delimiter =",")
    for line in csv_reader:
        print(line)

#Q2
# with open("CSV-starter/colours_20_simple.csv") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     for row in csv_reader:
#         print(f'{row[1]} {row[2]} {row[4]}')