<<<<<<< HEAD
# Bounding boxes form points

Write a function `bounding_box()` which takes a list of coordinates as an argument and returns a 100x100 array which is valued zero everywhere except for at the edges of the smallest rectagle containing every point (inclusive of the edge coordinates). 

You should also write a funcoitn which produces a list of random coordinates to test your function. 
### Example 
The example below is plotted onto a 10x10 array, rather than 100x100. We assume the cooordinates are zero indexed.

input:
`coordinates=[(2,3), (4,9), (1,5), (4,2)]`

expected output:
```
>>> bounding_box(coordinates)
[
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,1,1,1,1,0,0,0,0,0],
[0,1,0,0,1,0,0,0,0,0],
[0,1,0,0,1,0,0,0,0,0],
[0,1,0,0,1,0,0,0,0,0],
[0,1,0,0,1,0,0,0,0,0],
[0,1,0,0,1,0,0,0,0,0],
[0,1,0,0,1,0,0,0,0,0],
[0,1,1,1,1,0,0,0,0,0],
]
```
You can assume that every coordinate in the list has (x,y) values < 100, and that every coordinate is unique. 
=======
# Bounding boxes form points

Write a function `bounding_box()` which takes a list of coordinates as an argument and returns a 100x100 array which is valued zero everywhere except at the edges of the smallest rectagle containing every point (inclusive of the edge coordinates). 

You should also write a function which produces a list of random coordinates to test your function. 
### Example 
The example below is plotted onto a 10x10 array, rather than 100x100. We can assume the cooordinates are zero indexed.

input:
`coordinates=[(2,3), (4,9), (1,5), (4,2)]`

expected output:
```
>>> bounding_box(coordinates)
[
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,1,1,1,1,0,0,0,0,0],
[0,1,0,0,1,0,0,0,0,0],
[0,1,0,0,1,0,0,0,0,0],
[0,1,0,0,1,0,0,0,0,0],
[0,1,0,0,1,0,0,0,0,0],
[0,1,0,0,1,0,0,0,0,0],
[0,1,0,0,1,0,0,0,0,0],
[0,1,1,1,1,0,0,0,0,0],
]
```
You can assume that every coordinate in the list has (x,y) values < 100, and that every coordinate is unique. 
>>>>>>> 937cb3eb0189a1f738d9e7f8f4f56d12b901dfe3
