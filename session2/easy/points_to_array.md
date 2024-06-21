<<<<<<< HEAD
# Coordinates to array
Write a function `coordinates_to_array()` which takes a list of coordinates as an argument and returns a 100x100 array which has value 1 at the specified coordinates and value 0 everywhere else. 
### Example
In the example below the co-ordinates have been plotted onto a 10x10 array, rather than 100x100. Assume the coordinates are zero-index (i.e. the coordinates (0,0) indicates row-1 column-1.)

input:
`coordinates=[(2,3), (4,9), (1,5), (4,2)]`

expected output:
```
>>> coordinates_to_array(coordinates)
[
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,1,0,0,0,0,0],
[0,0,1,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,1,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,1,0,0,0,0,0],
]
```
You can assume that every coordinate in the list has (x,y) values < 100, and that every coordinate is unique.

### Bonus
Write a function which generates random lists of coordinates to plot, and a function which displays them with matplotlib.
=======
# Coordinates to array
Write a function `coordinates_to_array()` which takes a list of coordinates as an argument and returns a 100x100 array which has value 1 at the specified coordinates and value 0 everywhere else. 
### Example
In the example below the co-ordinates have been plotted onto a 10x10 array, rather than 100x100. Assume the coordinates are zero-index (i.e. the coordinates (0,0) indicates the first column of the first row.)

input:
`coordinates=[(2,3), (4,9), (1,5), (4,2)]`

expected output:
```
>>> coordinates_to_array(coordinates)
[
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,1,0,0,0,0,0],
[0,0,1,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,1,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,1,0,0,0,0,0],
]
```
You can assume that every coordinate in the list has (x,y) values < 100, and that every coordinate is unique.

### Bonus
Write a function which generates random lists of coordinates to plot, and a function which displays them with matplotlib.
>>>>>>> 937cb3eb0189a1f738d9e7f8f4f56d12b901dfe3
