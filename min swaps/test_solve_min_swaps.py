import unittest
import random
import solve_min_swaps

class TestMinSwaps(unittest.TestCase):
    nums = list()
    swaps = None

    @classmethod
    def setUpClass(self):
        self.nums = list()
        self.swaps = 0
        n = random.randint(4, 10)
        for i in range(0, n):  # create nums
            self.nums.append(i + 1)
        i = 0
        swapThese = list()
        for j in range(0, n):
                if random.randint(0, 99) > 45:
                    swapThese.append(j+1)
                    
                if len(swapThese) == 2:
                    l = swapThese.pop()
                    r = swapThese.pop()
                    self.nums[r-1] = l
                    self.nums[l-1] = r
                    self.swaps += 1
        print(self.nums)
        print("NUMS & SWAPS ->", n, self.swaps)

    @classmethod
    def tearDownClass(self):
        nums = list()
        self.swaps = None

    def test_correctness(self):
        assert solve_min_swaps.minimumSwaps(self.nums) == self.swaps

if __name__ == "__main__":
    unittest.main()
