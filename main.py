import csv

def load_file(file_name):
    try:
        with open(file_name) as file:
            file_data = [row for row in csv.DictReader(file)]
    # parent of IOError, OSError *and* WindowsError where available
    except EnvironmentError as e:
        print(e)
    else:
        return file_data

def main():
    filename = "example.csv"
    file_data = load_file(filename)

    reader(file_data)

def reader(file_data):
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