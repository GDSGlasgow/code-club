# standrd librayr imports
import sys
import random
sys.path.append('..')
# third party imports
import numpy as np
# local imports
from easy.functions import generate_points, points_to_array
from medium.functions import bounding_box

def random_array(n:int=100, array_shape:tuple[int]=100)->np.array:
    """Generates a random array with zeros and n ones. 

    Args:
        n (int, optional): Number of ones. Defaults to 100.
        array_shape (tuple[int], optional): output array shape. Defaults to 100.

    Returns:
        np.array: an array of shape array_shape, randomly valued as ones and zeros
    """
    points = generate_points(n, array_shape)
    return points_to_array(points, array_shape)

def array_to_box(array:np.array)->np.array:
    """An overly complicated function which I wrote before looking up the 
    np.argwhere function available from numpy. Puts a minumum bounding box 
    around the points in an array.
    
    Args:
        array (np.array): an array of ones and zeros to be bounded.

    Returns:
        np.array: the minimum box bounding the points in array.
    """
    n_cols, n_rows = np.shape(array)
    # sum up the rows and columns
    row_sums = [np.sum(array[:, x]) for x in range(n_cols)]
    col_sums = [np.sum(array[y, :]) for y in range(n_rows)]
    # pair with indices
    row_sums_idx = enumerate(row_sums)
    col_sums_idx = enumerate(col_sums)
    # get indices of non zero sum row sand columns
    non_zero_row_idx = [x[0] for x in row_sums_idx if x[1]>=1]  
    non_zero_col_idx = [x[0] for x in col_sums_idx if x[1]>=1]   
    # bound box is min and max values of these arrays
    min_x = non_zero_col_idx[0]
    max_x = non_zero_col_idx[-1]
    min_y = non_zero_row_idx[0]
    max_y = non_zero_row_idx[-1]
    # get the corner coordinates of the box
    box_coords = [(min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)]
    array_out = bounding_box(box_coords, (n_rows, n_cols))
    return array_out

def better_array_to_box(array:np.array)->np.array:
    """A much simpler function which uses the np.argwhere function to bound the
    points in the input array. 

    Args:
        array (np.array): an array of ones and zeros to be bounded.

    Returns:
        np.array: an array showing the minimum bounding box of the input.
    """
    points = np.argwhere(array) # returns non-zero indices
    array_out = bounding_box(points) # from the medium problem
    return array_out