import csv

# reading from csv file
# file = open("out.txt")
# csv_file = csv.reader(file)
# for row in csv_file:
#     name, phone, role = row
#     print(name)


# writing into csv file
# hosts = [["workstation.local", "192.168.107.234"], ["webserver.cloud", "192.168.107.188"]]
# with open("hosts.csv", "w") as hosts_csv:
#     writer = csv.writer(hosts_csv)
#     writer.writerows(hosts)


# reading file as dictCSV
# with open("hosts.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print("{} has {} users.".format(row["name"], row["users"]))


# writing file as dictCSV
# users = [{"name": "Antor", "username": "antor", "department": "CSE"},
#          {"name": "Jamil", "username": "jamil", "department": "IIT"},
#          {"name": "Shatil", "username": "satil", "department": "EEE"}]
#
# keys = ["name", "username", "department"]
#
# with open("hosts.csv", "w", newline="") as file:
#     writer = csv.DictWriter(file, fieldnames=keys)
#     writer.writeheader()
#     writer.writerows(users)


import os
import csv


# Create a file with data in it
def create_file(filename):
    with open(filename, "w") as file:
        file.write("name,color,type\n")
        file.write("carnation,pink,annual\n")
        file.write("daffodil,yellow,perennial\n")
        file.write("iris,blue,perennial\n")
        file.write("poinsettia,red,perennial\n")
        file.write("sunflower,yellow,annual\n")


# Read the file contents and format the information about each row
def contents_of_file(filename):
    return_string = ""

    # Call the function to create the file
    create_file(filename)

    # Open the file
    with open(filename) as file:
        # Read the rows of the file into a dictionary
        reader = csv.DictReader(file)
        # Process each item of the dictionary
        for row in reader:
            return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
    return return_string


# Call the function
print(contents_of_file("flowers.csv"))
