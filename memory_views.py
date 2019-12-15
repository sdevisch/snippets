import numpy as np

a = np.arange(6)
''' >>>
>>> a
>>> a.flags
>>> a.stride
'''
#  array([0, 1, 2, 3, 4, 5])
#  There is only one column, so the data is both row and f continuous
#  C_CONTIGUOUS : True
#  F_CONTIGUOUS : True
#  OWNDATA : True

a = np.arange(6).reshape(2, 3)
# array([[0, 1, 2],
#        [3, 4, 5]])
# C_CONTIGUOUS : True  # the data is arranged by row; data in the different columns is next to each other
# F_CONTIGUOUS : False
# OWNDATA : False; numpy changed the view, this reshaped version does not own the data
# strides: (24, 8)

a = np.arange(6).reshape(2, 3).T
# array([[0, 3],
#        [1, 4],
#        [2, 5]])
# C_CONTIGUOUS: False
# F_CONTIGUOUS: True
# OWNDATA: False
# strides: (8, 24)

a = np.arange(0, 32, 2)
# C_CONTIGUOUS: True # numpy created this straight
# F_CONTIGUOUS: True
# OWNDATA: True

a = np.arange(32)[::2]
# C_CONTIGUOUS: False
# F_CONTIGUOUS: False
# OWNDATA: False
# strides (16,)

a = np.arange(5)[::-1]
# C_CONTIGUOUS: False
# F_CONTIGUOUS: False
# OWNDATA: False
# strides (-8,)
