from typing import List, Optional
import itertools, random

class ShuffleIterator:
    def __init__(self, values: List[int], num_shuffles: Optional[int] = None):
        if num_shuffles is None:
            num_shuffles = float('inf')
        self.num_shuffles = num_shuffles
        self.i = 0
        self.all_perm = list(itertools.permutations(values))

    def __next__(self):
        if self.i >= self.num_shuffles:
            raise StopIteration
        t = random.choice(self.all_perm)
        self.i += 1
        return t
    def __iter__(self):
        return self

if __name__=='__main__':
    #for permutation in ShuffleIterator([1, 2, 3]):
    #    print(permutation)
    for permutation in ShuffleIterator([1, 2, 3], num_shuffles=10):
        print(permutation)