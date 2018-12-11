import numpy
import csv

def readCsvFile(file_name):
    with open(file_name) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        table = []
        for row in readCSV:
            table=row
        return table


def main():
    v = []
    adjacante_matrix = readCsvFile("Adjacante_matrice.csv")
    v = readCsvFile("Personnalisation_Student27.csv")

    print(v)
    return 0

if __name__ == '__main__':
    main()






"""A : np . matrix , alpha : f l o a t , v : np . array , m: bool"""
def itemRank(a, alpha, v, m):
    return None
