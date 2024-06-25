# Part 2: Falling sand in 2d
In this part, we will use the `Grain` class developed in part 1 to model the behaviour of multiple falling grains. We will consider sand falling onto an empty $21 \times 50$ array. A grain of sand is generated at location $(10,49)$ every 5 time steps. The physics of the sand are the same as in the previous section. 

Use multiple instances of your `Grain` class to find out the status of the array at $t=100$, $t=500$ and $t=2500$. 

## Extension
How do your outputs differ if the starting position of the grain is now selected at a random position on the first row? What if the starting position is selected by a random walK, i.e. if position $p_t = (i, 49)$ then $p_{t+1} = (i \pm 1, 49)$ ?
