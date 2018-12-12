import numpy as np
import csv


def readCsvFile(file_name):
    with open(file_name) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        table = []
        for row in readCSV:
            table.append(list(map(float, row)))
        return table


def prob_matrix(a):
    p = None
    for li in a:
        value = np.sum(li)
        if value != 0:
            if p is None:
                p = np.array([np.divide(li, value)])
            else:
                p = np.append(p, np.array([np.divide(li, value)]), axis=0)
    return p


def recur_res(p, a, x, v):
    next_x = np.multiply(a, p)
    next_x = np.dot(next_x, x)
    next_x = np.add(next_x, np.multiply(1 - a, v))

    if np.equal(x, next_x).all():
        return x
    else:
        return recur_res(p, a, next_x, v)


"""A : np . matrix , alpha : f l o a t , v : np . array , m: bool"""
def itemRank(a, alpha, v, m):
    p = np.transpose(prob_matrix(a))
    if m:
        """récurence"""
        return recur_res(p, alpha, v, v)
    else:
        """inversion matricielle"""
        I = np.identity(len(a[0]))
        matrix_inv = np.linalg.inv(np.subtract(I, np.multiply(alpha, p)))
        return np.multiply(1-alpha, np.dot(matrix_inv, v))


def main():
    a = np.array(readCsvFile("Adjacante_matrice.csv"))
    v = np.array(readCsvFile("Personnalisation_Student27.csv")[0])
    x = itemRank(a, 0.15, v, True)
    print("récurence ->", x)
    x = itemRank(a, 0.15, v, False)
    print("matricielle ->", x)

    return 0


if __name__ == '__main__':
    main()
