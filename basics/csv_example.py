import csv


with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["transaction_id", "product_id", "price"])
    writer.writerow([1000, 1, 5])
    writer.writerow([1001, 65, 45])

# for reading
with open("data.csv") as file1:
    reader = csv.reader(file1)
    for row in reader:
        print(row)
    # print(list(reader))
