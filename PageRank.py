import numpy
import csv

def readCsvFile(file_name):
    with open(file_name) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        table = []
        for row in readCSV:
            table.append(row)
        return table


def main():
    adjacante_matrix = readCsvFile("Adjacante_matrice.csv")
    print("adja ->",adjacante_matrix)
    v = readCsvFile("Personnalisation_Student27.csv")[0]
    print("v -> ",v)
    return 0

if __name__ == '__main__':
    main()






"""A : np . matrix , alpha : f l o a t , v : np . array , m: bool"""
def itemRank(a, alpha, v, m):
    return None
