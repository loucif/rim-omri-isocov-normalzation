# Filename: test_normalisation_fuc.py
# Description: test script on normalisation function RIM, OMRI, ISOCOV
# Authors: Loucif ghr.

import numpy as np
import normalisation_fuc as nrm

# performances of the alternatives
x = np.array([  [8, 7, 2, 1, 7], 
                [5, 3, 7, 5 , 1], 
                [7, 5, 6, 4 , 1],
                [9, 9, 7, 3 , 1], 
                [11, 10, 3, 7 , 1], 
                [6, 9, 5, 4 , 1]])

print('RIM Normalisation')
print(nrm.rim_normalisation(x, np.array([[4, 4, 4, 4, 4], [6, 6, 6, 6, 6]])))
print('OMRI Normalisation')
print(nrm.omri_normalisation(x, np.array([[4, 4, 4, 4, 4], [6, 6, 6, 6, 6]])))
print('ISOCOV Normalisation')
print(nrm.isocov_normalisation(x, np.array([[4, 4, 4, 4, 4], [6, 6, 6, 6, 6]]), np.array([True, True, False, False, True])))