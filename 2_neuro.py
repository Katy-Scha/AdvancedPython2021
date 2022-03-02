import pandas as pd
import numpy as np

pathA = input()
pathb = input()
x = list(map(float, input().split()))
with open(pathA) as fileA, open(pathb) as fileb:
    b = fileb.readlines()[0].split() #->str numbers in list
    b = np.array([list(map(float, b))]).T
    x = np.array([x])
    A = np.array(list(list(map(float, line.split())) for line in fileA))
    # Из усл.:"нужно возвести данную матрицу A в квадрат" - значит, А - квадратная матрица и x и b одной размерности.

    A2 = A.dot(A)
    res = (x.dot(A2)).dot(b)
    print(round(res[0][0], 16)) #убрать машинное эпсилон

