import numpy as np
import matplotlib.pyplot as plt

def rectilinear_distance(x,y):
    return sum(abs(a-b) for a,b in zip(x,y))

def score_matrix(x):
    """
    Input: x is tuple of query hospital location
    Output: dist/score matrix for the entire city for this hospital
    """
    scores = np.zeros((70, 70))
    for i in range(70):
        for j in range(70):
            scores[i,j] = rectilinear_distance((i,j), x)            
    return scores

def get_map(hospitals):
    allocations = np.empty((70,70), dtype=int)
    best_scores = np.ones_like(allocations)*np.inf
    for i in range(len(hospitals)):
        curr_scores = score_matrix(hospitals[i])
        allocations[curr_scores<best_scores] = i
        best_scores = np.minimum(best_scores, curr_scores)
    
    return allocations

def allocate_hospitals(locations):
    allocations = get_map(locations)
    plt.pcolor(allocations.T)
    plt.scatter(locations[:, 0], locations[:, 1])
    plt.axis('square')
    plt.show()

# INPUT: hospitals
hospitals = np.array([[50,40],[30,60]])
# SOLVE
allocate_hospitals(hospitals)