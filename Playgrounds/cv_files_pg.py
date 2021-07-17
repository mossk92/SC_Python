import csv

    # with open("data/2016_pilbara.csv") as csv_file #if file is not in same folder - need to express the lin
    #     csv_reader = csv.reader(csv_file, delimiter="-") #change delimiter to - instead of comma
    #     for line in csv_reader:
    #         print(line)

population = []

with open("2016_pilbara.csv", mode="r", encoding="utf-8") as csv_file: #if file is not in same folder - need to express the lin
    csv_reader = csv.reader(csv_file, delimiter="-") #change delimiter to - instead of comma
    for line in csv_reader:
        population.append(line)
       
print(population)

for age_group in population:
    print(f"{age_group[0]} {age_group[1]}")

with open("population.csv", mode="w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)