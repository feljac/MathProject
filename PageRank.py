import numpy as np
import csv


def readCsvFile(file_name):
    with open(file_name) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        table = []
        for row in readCSV:
            table.append(list(map(float, row)))
        return table


"""A : np . matrix , alpha : f l o a t , v : np . array , m: bool"""
def itemRank(a, alpha, v, m):
    if m:
        """récurence"""

    else:
        """inversion matricielle"""
        
    return 'None'


def prob_matrix(a):
    p = []
    for li in a:
        value = np.sum(li)
        print(value)
        if value != 0:
            p.append(np.divide(li, value).tolist())
    return p


def main():
    a = np.array(readCsvFile("Adjacante_matrice.csv"))
    print("A ->", a)
    v = np.array(readCsvFile("Personnalisation_Student27.csv")[0])
    print("v -> ", v)
    p = prob_matrix(a)
    print("P->",p)
    x = itemRank(a, 0.15, v, True)
    print(x)
    x = itemRank(a, 0.15, v, True)
    print(x)

    return 0


if __name__ == '__main__':
    main()
