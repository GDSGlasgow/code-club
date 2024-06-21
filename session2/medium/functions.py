import numpy as np

def bounding_box(points:list[tuple[int]], array_shape:tuple[int]=(100,100))->np.array:
    """Generates plots the minimum bounding box around a set of points as an
    array of ones and zeros.

    Args:
        points (list[tuple[int]]): the list of points to be bounded
        array_shape (tuple[int], optional): shape of the output array.

    Returns:
        np.array: an array valued as 1 at the bounding box and zero elsewhere.
    """
    # get the maximum and minimum x and y values
    bounds:dict = get_bounds(points)
    array_out:np.array = np.zeros(array_shape)
    # set the value of the array at the bounds as 1
    array_out[bounds['min_x'], bounds['min_y']:bounds['max_y']+1] = 1
    array_out[bounds['max_x'], bounds['min_y']:bounds['max_y']+1] = 1
    array_out[bounds['min_x']:bounds['max_x']+1, bounds['min_y']] = 1
    array_out[bounds['min_x']:bounds['max_x']+1, bounds['max_y']] = 1
    return array_out
    
    
def get_bounds(points:list[tuple[int]])->list:
    """Retreives the bounds froma list of coordinates
    args:
        points (list[tuple[int]]) : a list of coordinates.
    returns:
        dict[str,int] : the bounds of the coordinates.
    """
    min_x:int = np.amin([p[0] for p in points])
    min_y:int = np.amin([p[1] for p in points])
    max_x:int = np.amax([p[0] for p in points])
    max_y:int = np.amax([p[1] for p in points])
    return {'min_x':min_x, 'max_x':max_x, 'min_y':min_y, 'max_y':max_y}