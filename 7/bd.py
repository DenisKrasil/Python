from codecs import utf_16_decode
import csv


def read_data():
    with open('contact.csv', 'r') as file:
        y = csv.reader(file)
        data = [row for row in y]
    return data


def data_entry_to_file(x):
    with open("contact.csv", "a", newline='') as p:
        pr = csv.writer(p, dialect='excel', delimiter=";")
        pr.writerow(x)


def data_rewrite_to_file(x):
    with open("contact.csv", "w", newline='') as p:
        pr = csv.writer(p)
        pr.writerows(x)

def print_contact():
    with open('contact.csv', newline='') as File:
        reader = csv.reader(File)
        for row in reader:
            print(row)


