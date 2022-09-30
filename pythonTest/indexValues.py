from time import perf_counter
import torch
import random

def h():
    print('feng')
    # return 9
    yield 12
    print('yes')
if __name__ == '__main__':
    w = torch.normal(0, 0.01, (8,1), requires_grad=True)
    b = torch.zeros(1, requires_grad=True)
    print(w)
    print(b)