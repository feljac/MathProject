import numpy as np
import csv


def readCsvFile(file_name):
    """Open a csv file and convert it's content to an array"""
    with open(file_name) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        array = []
        for row in readCSV:
            array.append(list(map(float, row)))
        return array


def prob_matrix(a):
    """Convert an adjacence matrix to a transition probability matrix"""
    p = None
    for li in a:
        value = np.sum(li)
        if value != 0:
            if p is None:
                """first create the matrix"""
                p = np.matrix(np.divide(li, value))
            else:
                """append lines to the matrix"""
                p = np.append(p, np.matrix(np.divide(li, value)), axis=0)
    return p


def recur_res(p, a, x, v):
    """Recursive method for itemRank"""
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
    """transpose and normalise the vector"""
    vectore_norm_transp = np.transpose(np.divide(v, np.sum(v)))
    """convert the vector to a matrix"""
    vector_as_matrix = np.reshape(vectore_norm_transp, (10, 1))
    if m:
        """récurence"""
        result = recur_res(p, alpha, vector_as_matrix, vector_as_matrix)
        return np.squeeze(np.asarray(result))
    else:
        """inversion matricielle"""
        I = np.identity(a.__len__())
        matrix_inv = np.linalg.inv(np.subtract(I, np.multiply(alpha, p)))
        result = np.multiply(1-alpha, np.dot(matrix_inv, vector_as_matrix))
        return np.squeeze(np.asarray(result))

def main():
    a = np.matrix(readCsvFile("Adjacante_matrice.csv"))
    v = np.array(readCsvFile("Personnalisation_Student27.csv")[0])
    x = itemRank(a, 0.15, v, True)
    print("récurence ->", x)
    x = itemRank(a, 0.15, v, False)
    print("matricielle ->", x)
    return 0


if __name__ == '__main__':
    main()
