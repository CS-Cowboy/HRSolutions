def solve_knapsack(profits, weights, capacity):
  c = capacity
  totalProfits = list()
  solution = list()
  i = len(profits)-1
  while(i > 1):
    c = c - weights[i]

    if weights[i-1] <= c:
      totalProfits.append(profits[i-1])
      solution.append(weights[i-1])
    i-=1
  sum = 0
  for profit in totalProfits:
      sum += profit
  print(solution)
  print(sum)

solve_knapsack([1,6,10,16], [1,2,3,5], 7)