import torch
import random

def h():
    print('feng')
    # return 9
    yield 12
    print('yes')
if __name__ == '__main__':
    test_batch = [[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6]]
    h()