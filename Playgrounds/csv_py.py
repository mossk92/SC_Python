import csv 

    # with open("dogs_are_awesome.txt", mode = "r", encoding = "utf-8") as csv_file: #mode r = read (w = write)
    #                             #mode r and encoding utf-8 are default position so are not actually needed
    #                             #csv_file is arbitrary name, could be anything
    #     csv_reader = csv.reader(csv_file, delimiter=",") # creates the reader object
    #                 #goes through the file lie by line and creates a list per line
    #                 #delimiter is a default position also so not needed but can be changed if needed
    #     for line in csv_reader:
    #         print(line)

asli_said = [] #not sure what this was doing

with open("dogs_are_awesome.txt", mode = "r", encoding = "utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for line in csv_reader:
        print(line)
        asli_said.append(line)

print(asli_said)

with open("asli_says.txt", mode="w", newline="") as csv_file: #if txt file does not exist, it will create, if it does exist - it will ammend
                            #newline helps with handling of
    csv_writer = csv.writer(csv_file) #creates the writer object
    for item in asli_said:
        csv_writer.writerow(item) #strings or lists