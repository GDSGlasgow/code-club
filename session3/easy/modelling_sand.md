# Modelling Sand
In this Code Club session we are going to try to model falling sand using object oriented programming (OOP). In this first task we will aim to construct a class (or object) which can model the behaviour of falling sand under different conditions. 

If you are new to OOP you can find information classes and objects in Python [here](https://www.geeksforgeeks.org/python-classes-and-objects/).

# Falling Sand
For this first task we will try to model the behaviour of a single peice of sand in multiple scenarios. We will model the behaviour of the sand on a 11x10 array with the grain taking up exactly one cell in that array. This description assumes the array is zero indexed, and uses $i$ and $j$ to refer to horizontal and vertical indices, resprectively. 

The grain will start at position $(5,0)$, and falling one cell vertically down at each timestep, so that at time $t=0$ the position is $(5,0)$, then at $t=1$ we have $(5,1)$ and so on. The grain falls like this until its path is blocked by either the bottom of the array (i.e. any position $(i,9)$) or another (stationary) grain of sand.

There are three posible outcomes when the grain reaches a second grain of sand. Consider a falling grain at position $(i,j)$, which has fallen on top of a second grain at position $(i,j+1)$. The grain can then move diagonally into cells $(i-1,j+1)$ or $(i+1,j+1)$ if they are (a) not occupied by abother grain and (b) not beyond the boundary of the array $i<0$ or $i>10$. Hence, the three possible moves are:

1. If both cells $(i-1, j+1)$ and $(i+1, j+1)$ are available, the grain moves into either cell with probability $p=0.5$.
2. If only one of cells $(i-1, j+1)$ or $(i+1, j+1)$ are available, the grain moves into the the empty cell with probability $p=1$.
3. If neither cells $(i-1, j+1)$ or $(i+1, j+1)$ are available, the grain comes to rest in its current position.

# Building a `Grain` of sand
Create a `Grain()` class which can model this behaviour. It should have attributes indicating its current position and whether it is currently at rest. The class should also include a `time_step()` method which takes an array as an argument, and updates the grains position according to the surrounding cells.

For example, consider a grain initialised as:

`>>> grain = Grain(i=5, j=0)`

With an array initialised as:
`>>> array = np.zeros((11,10))`

Then we would expect the following behaviour:
```
>>> grain.time_step(array)
>>> grain.i
5
>>> grain.j
1
>>> for ii in range(8):
...     grain.time_step(array)
>>> grain.i
5
>>> grain.j
9
>>> grain.time_step(array)
>>> grain.i
5
>>> grain.j # noting grain is now at bottom of array.
9
>>> grain.is_stationary
True
```

And the following behaviour when the grain is in contact with another grain at $(5,0)$
```
>>> array = np.zeros((11,1))
>>> array[5,0] = 1 # add a grain at (5,0)
>>> grain = Grain(5,1) # initialise to cell above existing grain
>>> grain.time_step(array)
>>> grain.i
4
>>> grain.j
0
>>> grain.is_stationary
True
```
Noting that either $(4,0)$ or $(6,0)$ would be valid locations in this instance. Other behaviour, such as what happens at the boundary of the array, follows in a similar way.