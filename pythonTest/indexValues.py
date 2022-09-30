from time import perf_counter
import torch
import random

def h():
    print('feng')
    # return 9
    yield 12
    print('yes')
if __name__ == '__main__':
    test_ = torch.randn(2,3)
    print(test_)
    print(test_.shape)