<<<<<<< HEAD
# Bounding boxes from arrays

Write a function `bounding_box_from_array() which takes a 100x100 array as an argument with values of either 0 or 1 at each point, and returns a new 100x100 array, which is valued 0 everywhere except the edges of the smallest box containing every 1 in the original array.

You should also write a function which can generate random arrays to test your function. 
### Example
input:
```
array=[
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
output:
```
>>> bounding_box_from_array(array)
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
You can assume that the input array will always be 100x100 and have valued as either 0 or 1.
=======
# Bounding boxes from arrays

Write a function `bounding_box_from_array()` which takes a 100x100 array as an argument with values of either 0 or 1 at each point, and returns a new 100x100 array, which is valued 0 everywhere except the edges of the smallest box containing every 1 in the original array.

You should also write a function which can generate random arrays to test your function. 
### Example
input:
```
array=[
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
output:
```
>>> bounding_box_from_array(array)
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
You can assume that the input array will always be 100x100 and have valued as either 0 or 1.
>>>>>>> 937cb3eb0189a1f738d9e7f8f4f56d12b901dfe3
