import pandas as pd
import numpy as np

N, M = map(int, input().split())
data = []
for i in range(N):
    t = list(map(int, input().split()))
    data.append(t)
data = pd.DataFrame(data)
print(((data<-5).sum()).sum()) #сумма логических значений по всей табл

print(int(-(data[data<0]).sum().sum()))

print(data.max().max())
