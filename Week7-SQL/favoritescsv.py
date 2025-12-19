import csv

with open("favorites.csv", "a") as file:
    while True:
        time = input("Timestamp: ")
        language = input("Language: ")
        problem = input("Problem: ")

        writer = csv.DictWriter(file, fieldnames=["Timestamp", "language", "problem"])
        writer.writerow({"Timestamp": time, "language": language, "problem": problem})