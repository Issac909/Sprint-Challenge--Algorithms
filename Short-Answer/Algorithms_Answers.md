#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Polynomial time complexity


b) Quadratic time complexity


c) Logarithmic time complexity

## Exercise II
- The following code is Linear Time Complexity:
From n, which is the maximum floor(height) of the building, we can determing the midpoint(mid = n // 2). After the midpoint is set up, we can drop an egg and check if it will break. 
  If the midpoint is enough for the egg to break, set new height to be from that midpoint, then make another midpoint from based on the new height

    If the egg doesn't break at the midpoint, move the height up (n + 1), until it does break. At the first egg to break while the height increases, return floor number(f)

