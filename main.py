import csv

def main():
    filename = "example.csv"


    reader(filename)

def reader(file_name):
    with open(file_name) as file:
        file_data = [row for row in csv.DictReader(file)]


    header = file_data[0].keys()
    print(header)
    print(file_data)

    for row in file_data:
        test = row
        print(row)
        if row["field1"] == "row2item1":
            print("found")

if __name__=="__main__":
    main()