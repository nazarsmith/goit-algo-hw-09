# goit-algo-hw-09

## Task:

1. Find the optimum solution for the change (knapsack) problem (give an amount of change given a set of coins) using a `greedy` approach as well as `dynamic` programming;
2. Solve the problem for a larger change amount (**20,000** cents in this experiment);
3. Time both algorithms;

## Results:

### Total coins (GREEDY): {50: 400, 25: 0, 10: 0, 5: 0, 2: 0, 1: 0}

- Total change assembled GREEDY: 20000
- Execution time (GREEDY): 0.001

### Total coins (DYNAMIC): {50: 400, 25: 0, 10: 0, 5: 0, 2: 0, 1: 0}

- Total change assembled DYNAMIC: 20000
- Execution time (DYNAMIC): 8.24

The following results can be observed:

- both algorithms solved the task successfully - the required change amount is assmbled in both cases:
- however, the `greedy` algortithm completed the task markedly faster - within 0.001 sec (as compared to `dynamic` - 8.24 sec);
- at the same time, both algorithms work comparably fast with tasks that involve smaller numbers (to assemble 200 cents of change) - 0 sec for `greedy` VS 0.002 sec for `dynamic`;
- the main source of such delays when it comes to applying an algorithm based on `dynamic` programming to knapsack problems seems to be the fact that the sum of the choice items from which the knapsack is to be filled must be at least equal to the knapsack volume (unless the memory table construction and fillup is **heavily modified**, the algorithm will fail to find the optimum solution (e.g. if the knapsack can carry 20 kg, but the sum of the choice items equals 10 kg. In such a case, the `dynamic` algorithm will simply put everything inside. `Greedy` algorithms are more flexible as they can be modified fairly easily)).
- additionally, the implementation of greedy algorithm is much easier to read as it is straightforward (compared to the memo tables that dynamic programming relies on)
