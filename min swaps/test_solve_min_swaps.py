import unittest
import random
import solve_min_swaps

class TestMinSwaps(unittest.TestCase):
    nums = list()
    validResults = None

    @classmethod
    def setUpClass(self):
        print("Enter your input file name: ")
        fn = str(input())
        file = open(fn, "r")
        
        print("Now enter your solution file name: ")
        sln = str(input())
        self.validResults = int(str(open(sln, "r").readline().strip()))
        
        print("Proceeding to read file and test...")
        lines = file.readlines()
        self.nums = list()
        for line in lines:
            for num in line.split():
                self.nums.append(int(num))
        file.close()
        print("len(numberList), validSolution ->", len(self.nums), self.validResults)

    @classmethod
    def tearDownClass(self):
        nums = list()
        self.swaps = None

    def test_correctness(self):
        assert solve_min_swaps.minimumSwaps(self.nums) == self.validResults

if __name__ == "__main__":
    unittest.main()
