# rim-normalzation
 Normalization approach defined to handle value constraints for MCDA methods

# Description : 
    RIM Normalisation : This normalization has been proposed by Cables and al It is the first normalization approach defined to handle value constraints. This normalization proceeds by dividing the distance between the performance ratings by the distance between the maximum (or the minimum) performance rating and the reference ideal performance rating for that criterion. The reference ideal, given generally as an interval [A, B], represents the value constraints fixed by the user for the criterion .
    OMRI Normalisation : Extention from RIM Normalisation.
    ISOCOV Normalisation : Another extention from RIM Normalisation with the introduction of the new argument cost-benefit for criterion.

# Usage :
    rim_normalisation(decision_matrix, AB).
    omri_normalisation(decision_matrix, AB).
    isocov_normalisation(decision_matrix, AB, is_it_benfit_then_it_would_be_cost).

# Arguments :
    decision_matrix : The decision matrix (m x n) with the values of the m alternatives, for the n criterion.
    AB : constraint matrix (2 x n). AB[0,:] corresponds with the A extrem, and AB[1,:] represents the B extrem of the domain of each criterion.
    is_it_benfit_then_it_would_be_cost : boolean matrix (2 x 1) with true for benifit criterion and false if it is a cost criterion.

# Value :
    It returns the new normalized desision matrix.

# References :

# Examples : 
    included in test_normalization.