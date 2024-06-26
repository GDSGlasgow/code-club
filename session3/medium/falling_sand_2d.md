# Part 2: Falling sand in 2d
In this part, we will use the `Grain` class developed in part 1 to model the behaviour of multiple falling grains. We will consider sand falling onto an empty $21 \times 50$ array. A grain of sand is generated at location $(10,49)$ every 5 time steps. The physics of the sand are the same as in the previous section. 

Use multiple instances of your `Grain` class to find out the status of the array at $t=100$, $t=500$ and $t=2500$. 

## Extension
1. How do your outputs differ if the starting position of the grain is now selected at a random position on the first row?
2. What if the starting position is selected by a random walk, i.e. if a grain is generated at position $p = (i, 49)$ then the next grain is generated at  $q = (i \pm 1, 49)$ ?
3. What happens if the dynamics are biased such that the probability of falling left is $P_l = 0.3$ and the probabilty of falling right is $P_r = 0.7$ ?
