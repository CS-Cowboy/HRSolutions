import sys
from typing import Reversible
weights = list()
profits = list()
totalCapacity = 99999

def binary_knapsack(memo, i, j, capacity, profit):
    i+=1
    if capacity > totalCapacity:
        w = weights[j]
        memo.remove(w)
        return memo, (profit - profits[j]), (capacity - w)

    if i == len(weights) - 1:
        return memo, profit, capacity

    m_1 = memo.copy()
    m_2 = memo.copy()

    m_1.append(weights[i])
    m_2.append(weights[i+1])

    t_1 = binary_knapsack(m_1, i+1, i, capacity +
                          weights[i], profit + profits[i])
    t_2 = binary_knapsack(m_2, i+1, i+1, capacity +
                          weights[i+1], profit + profits[i+1])
    if t_1[1] > t_2[1]:
        return t_1
    return t_2


if __name__ == "__main__":
    w = list(str(sys.argv[1]).split())
    p = list(str(sys.argv[2]).split())
    if len(w) == len(p):
        for i in range(len(w)):
            weights.append(int(w[i]))
            profits.append(int(p[i]))
        totalCapacity = int(str(sys.argv[3]))
        tup = binary_knapsack(list(), 0, 0, 0, 0)
        print(" Optimal choice ->",
              tup[0],"Profits -> ", tup[1], " Final capacity ->", tup[2])
