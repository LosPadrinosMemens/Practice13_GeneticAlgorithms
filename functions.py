def determine_domination(v1, v2):
    """
    Parameters
    - v1 (tuple):
    - v2 (tuple):

    Returns
    - Boolean
    """
    better_in_at_least_one = False
    no_worse_in_all = True
    
    for i in range(len(v1)):
        if v1[i] < v2[i]:
            better_in_at_least_one = True
        elif v2[i] < v1[i]:
            no_worse_in_all = False
            break

    v1_dominates = no_worse_in_all and better_in_at_least_one
    return v1_dominates

def naive_non_dominated(V):
    """
    Parameters
    - V (list of tuples): Objective vectors
    """
    S = set()
    
    for v in V:
        dominated = False
        for other in V:
            if other != v and determine_domination(other, v):
                dominated = True
                break
        if not dominated:
            S.add(v)

    return S

import csv

def read_csv_to_tuples(filename):
    """
    Parameters:
    - filename (str): The path to the CSV file.
    
    Returns:
    - list of tuples: The contents of the CSV file as a list of tuples.
    """
    data = []
    with open(filename, mode='r') as file:
        for line in file:
            row = tuple(map(float, line.strip().split()))
            data.append(row)
    return data

def define_layers(V):
    """
    Parameters
    - V (list of tuples): Objective vectors
    """

    list_layers = []

    set_V = set(V)
    i = 1
    while set_V:
        print(i)
        print(len(set_V))
        layer =  naive_non_dominated(set_V)
        print(len(layer))
        list_layers.append(layer)
        set_V -= layer
        i += 1

    return list_layers