import numpy as np
import random

# converting coordinates to arrays
def points_to_array(points:list[tuple[int]], shape:tuple[int]=(100,100))->np.array:
    """Plots a list of coordinates onto a grid of ones and zeros
    args:
        points (list[tuple[int]]) : a list of coordinates to plot.
        shape (tuple[int]) : the shape of the output array.
    returns:
        np.array : an array with 1 at the given points and zeros elsewhere.
    """
    array_out:np.array = np.zeros(shape)
    for px, py in points:
        array_out[px, py] = 1
    return array_out
    
def generate_points(n:int=100, array_shape:tuple[int]=(100,100))->list[tuple[int]]:
    """Generates n random location within the given array bounds.
    args:
        n (int) : the number of points to be generated.
        array_shape (tuple[int]) : the array size for the points.
    returns:
        list[tuple[int]] : a list of random coordinates inside array_shape.
    """
    points = []
    for i in range(n):
        px_i = random.randint(0, array_shape[0]-1)
        py_i = random.randint(0, array_shape[1]-1)
        points.append((px_i, py_i))
    return points