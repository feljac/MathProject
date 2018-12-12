import numpy as np
import csv


def readCsvFile(file_name):
    with open(file_name) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        table = []
        for row in readCSV:
            table.append(list(map(float, row)))
        return table


def prob_transpo_matrix(a):
    p = []
    for li in a:
        value = np.sum(li)
        if value != 0:
            p.append(np.divide(li, value).tolist())
    return np.transpose(p).tolist()


"""A : np . matrix , alpha : f l o a t , v : np . array , m: bool"""
def itemRank(a, alpha, v, m):
    p = prob_transpo_matrix(a)
    x = None
    if m:
        """récurence"""

    else:
        """inversion matricielle"""
        I = np.identity(len(a[0]))
        matrix_inv = np.linalg.inv(np.subtract(I, np.multiply(alpha, p)))
        x = np.multiply(1-alpha, np.dot(matrix_inv, v))
    return x


def main():
    a = np.array(readCsvFile("Adjacante_matrice.csv"))
    v = np.array(readCsvFile("Personnalisation_Student27.csv")[0])
    x = itemRank(a, 0.15, v, True)
    print(x)
    x = itemRank(a, 0.15, v, False)
    print(x)

    return 0


if __name__ == '__main__':
    main()
