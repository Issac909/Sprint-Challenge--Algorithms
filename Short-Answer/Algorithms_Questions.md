# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n): #0n^3
      a = a + n * n #0n^2
# The above code is Polynomial time complexity
```

```python
b)  sum = 0
    for i in range(n): # 0(n * (1 + (log n))) = 0(n * log n) = 0(n log n)
      j = 1 #0(1)
      while j < n: # 0(log n)
        j *= 2
        sum += 1
# The above code has Quadratic time complexity
```

```python
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1) # 0(1 + log n)
# The above code is Logarithmic time complexity
```

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.
