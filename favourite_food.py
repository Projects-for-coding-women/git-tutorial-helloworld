import csv

def list_favourite_food(filepath):

    with open(filepath) as csvfile:
        csv_reader = csv.reader(csvfile)
        # Skip the first row
        next(csv_reader)
        for row in csv_reader:
            print(f"{row[0]}'s favourite food is {row[1]}")

list_favourite_food("food/favourite_food.csv")