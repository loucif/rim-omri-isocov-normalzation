# Filename: normalisation_fuc.py
# Description: normalisation function RIM, OMRI, ISOCOV
# Authors: Loucif ghr.

import numpy as np

"""
Description : 
    RIM Normalisation : This normalization has been proposed by Cables and al It is the first normalization approach defined to handle value constraints. This normalization proceeds by dividing the distance between the performance ratings by the distance between the maximum (or the minimum) performance rating and the reference ideal performance rating for that criterion. The reference ideal, given generally as an interval [A, B], represents the value constraints fixed by the user for the criterion .
    OMRI Normalisation : Extention from RIM Normalisation.
    ISOCOV Normalisation : Another extention from RIM Normalisation with the introduction of the new argument cost-benefit for criterion.
Usage :
    rim_normalisation(decision_matrix, AB)
    omri_normalisation(decision_matrix, AB)
    isocov_normalisation(decision_matrix, AB, is_it_benfit_then_it_would_be_cost)
Arguments :
    decision_matrix : The decision matrix (m x n) with the values of the m alternatives, for the n criterion
    AB : constraint matrix (2 x n). AB[0,:] corresponds with the A extrem, and AB[1,:] represents the B extrem of the domain of each criterion
    is_it_benfit_then_it_would_be_cost : boolean matrix (2 x 1) with true for benifit criterion and false if it is a cost criterion
Value :
    It returns the new normalized desision matrix
References :
Examples :
"""

def rim_normalisation(decision_matrix, AB):
    
    AB = np.array(AB, dtype='float64')
    decision_matrix = np.array(decision_matrix, dtype='float64')
    decision_matrix_temp = np.array(decision_matrix, dtype='float64')

    for j in range(decision_matrix.shape[1]):
        for i in range(decision_matrix.shape[0]):
            if (AB[0, j] <= decision_matrix[i, j] <= AB[1, j]):
                decision_matrix_temp[i, j] = 1
            elif (np.min(decision_matrix[:, j]) <= decision_matrix[i, j] <= AB[0, j]):
                decision_matrix_temp[i, j] = 1 - (AB[0, j] - decision_matrix[i, j])/(AB[0, j] - np.min(decision_matrix[:, j]))
            else:
                decision_matrix_temp[i, j] = 1 - (decision_matrix[i, j] - AB[1, j])/(np.max(decision_matrix[:, j]) - AB[1, j])

    return decision_matrix_temp

def omri_normalisation(decision_matrix, AB):

    AB = np.array(AB, dtype='float64')
    decision_matrix = np.array(decision_matrix, dtype='float64')
    decision_matrix_temp = np.array(decision_matrix, dtype='float64')

    for j in range(decision_matrix.shape[1]):
        for i in range(decision_matrix.shape[0]):
            if (AB[0, j] <= decision_matrix[i, j] <= AB[1, j]):
                decision_matrix_temp[i, j] = 1
            elif (np.min(decision_matrix[:, j]) <= decision_matrix[i, j] <= AB[0, j]):
                decision_matrix_temp[i, j] = 1 - (AB[0, j] - decision_matrix[i, j])/max(AB[0, j] - np.min(decision_matrix[:, j]), np.max(decision_matrix[:, j]) - AB[1, j])
            else:
                decision_matrix_temp[i, j] = 1 - (decision_matrix[i, j] - AB[1, j])/max(AB[0, j] - np.min(decision_matrix[:, j]), np.max(decision_matrix[:, j]) - AB[1, j])

    return decision_matrix_temp

def isocov_normalisation(decision_matrix, AB, is_it_benfit_then_it_would_be_cost):

    AB = np.array(AB, dtype='float64')
    decision_matrix = np.array(decision_matrix, dtype='float64')
    decision_matrix_temp = np.array(decision_matrix, dtype='float64')

    for j in range(decision_matrix.shape[1]):
        for i in range(decision_matrix.shape[0]):
            if is_it_benfit_then_it_would_be_cost[j]:
                if (AB[0, j] <= decision_matrix[i, j] <= AB[1, j]):
                    decision_matrix_temp[i, j] = 1
                elif (np.min(decision_matrix[:, j]) <= decision_matrix[i, j] <= AB[0, j]):
                    decision_matrix_temp[i, j] = 1 - (AB[0, j] - decision_matrix[i, j])/(max(AB[0, j] - np.min(decision_matrix[:, j]), np.max(decision_matrix[:, j]) - AB[1, j]) + 1)
                else:
                    decision_matrix_temp[i, j] = 1 - (1 + decision_matrix[i, j] - AB[1, j])/(max(AB[0, j] - np.min(decision_matrix[:, j]), np.max(decision_matrix[:, j]) - AB[1, j]) + 1)
            else:
                if (AB[0, j] <= decision_matrix[i, j] <= AB[1, j]):
                    decision_matrix_temp[i, j] = 1/(max(AB[0, j] - np.min(decision_matrix[:, j]), np.max(decision_matrix[:, j]) - AB[1, j]) + 1)
                elif (np.min(decision_matrix[:, j]) <= decision_matrix[i, j] <= AB[0, j]):
                    decision_matrix_temp[i, j] = (AB[0, j] - decision_matrix[i, j])/max(AB[0, j] - np.min(decision_matrix[:, j]), np.max(decision_matrix[:, j]) - AB[1, j])
                else:
                    decision_matrix_temp[i, j] = (decision_matrix[i, j] - AB[1, j])/max(AB[0, j] - np.min(decision_matrix[:, j]), np.max(decision_matrix[:, j]) - AB[1, j])
    
    return decision_matrix_temp