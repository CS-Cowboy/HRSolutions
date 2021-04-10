import sys
from typing import Dict


targetVal = 0
nums = list()


def solve_equal_subset_partition(memo, sums, n, i):
    K = i + 1
    if i == len(nums) or sums[K] == targetVal:
        return memo[i]

   # print("new call-> ", memo, sums, n, i, '\n')
    for N in nums:
        if N == n:
            continue
        if sums[K] + N <= targetVal:
            memo[K].append(N)
            sums[K] += N
   # print('MEMO->\t\t\t', memo, "\n")
    if sums[K] == targetVal:
        for F in memo[K]:
            nums.remove(F)
        return nums, memo[K]
    else:
        return solve_equal_subset_partition(memo,  sums, nums[i], K)


if __name__ == "__main__":
    sum = 0
    if len(sys.argv) > 1:
        numList = str(sys.argv[1]).split()
        for n in numList:
            sum += int(n)
            nums.append(int(n))
        if sum % 2 == 0:
            targetVal = int(sum / 2)
            print("Target  (must be even whole number)  -> ", targetVal)
            memo = dict()
            sums = dict()
            j = 0
            for j in range(len(nums)):
                    memo.update({nums[j]: list()})
                    sums.update({nums[j]: 0})
            print("Partition Solution ->  ", solve_equal_subset_partition(memo, sums, nums[0], 0), " Both partitions now add to:  ", targetVal, '    =^_^=')
        else:
            print("Impossible!")
    else:
        print('Please supply argument:   <number list>')
