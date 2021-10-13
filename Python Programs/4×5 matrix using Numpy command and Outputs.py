#X2= array([[34, 5, 7, 4, 13],[ 8, 6, 11, 8, 12 ],[ 9, 6, 5, 3, 17],[7, 9, 8, 2, 13]])

#a). np.concatenate( [X2,X2],axis=1)
#b). np.vstack([X2,X2])
#c). np.hstack([X2,X2])

import numpy as np
X2= np.array([[34, 5, 7, 4, 13],
[ 8, 6, 11, 8, 12 ],
[ 9, 6, 5, 3, 17],
[7, 9, 8, 2, 13]])
print("a)",np.concatenate([X2,X2],axis=1))
print("\r")
print("b)", np.vstack([X2,X2]))
print("\r")
print("c)", np.hstack([X2,X2]))
