# Paet 3: Falling sand in 3d
We will now update our `Grain` class to model sand falling on to a $51 \times 51$ cell surface, from a height of $50$ cells. In this instance, a grain at position $p_t=(i, j, k)$ will fall to position $p_{t+1} = (i, j, k-1)$, assuming (a) the new cell is empty and (b) $k > 0$. A grain of sand at position $p_t=(i,j,k)$ falling on top of a stationary grain of sand at position $q=(i,j,k-1)$ can now move into any of the four cells orthogonally adjacent to $q$, that is: $(i+1,j,k-1)$, $(i-1, j, k-1)$, $(i, j+1, k-1)$, $(i, j-1, k-1)$, with equal probability, assuming they are all available and $i$ and $j$ are not at the array boundary.  

Assuming grains are generated at cell $p_0=(25, 25, 50)$ every 5 time steps, output the status of the array at $t=100$, $t=500$ and $t=2500$. You may choose how best to visualise your output arrays.

# Extension
1. How do the output arrays change if an impeded cell at $p_t = (i,j,k)$ can fall into any of the eight orthogonally **OR** diagonally adjacent cells to $q=(i,j,k-1)$?
2. What happens if the grains are generated at a random location on the $k=50$ plane?
3. What happens if grain generation points are selected by a random walk, i.e. if $p_0 = (i,j,50)$ then $q_0 = (i \pm 1, j, 50)$ or $(i, j \pm1, 50)$?
