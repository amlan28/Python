#X = array([0, 1,2, 3, 4, 5, 6, 7, 8, 9])
#a. X[1:7:2]
#b. X[-2:10]
#c. X[-3:3:-1]
#d. X[5:]
#e. X[1::2]


import numpy as np
X =np.array([0, 1,2, 3, 4, 5, 6, 7, 8, 9])
print("a)",X[1:7:2])
print("b)",X[-2:10])
print("c)",X[-3:3:-1])
print("d)",X[5:])
print("e)",X[1::2])
