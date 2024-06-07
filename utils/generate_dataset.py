import torch
from torch.autograd import Variable
import numpy as np


def generate_linear_data(n_data: int, coeff:float = 2, intercept:float = 1):
    # create dummy data for training
    x = np.array([i for i in range(n_data)], dtype=np.float32)
    x = x.reshape(-1, 1)

    y = np.array([coeff*i + intercept for i in x], dtype=np.float32)
    y = y.reshape(-1, 1)

    x = Variable(torch.from_numpy(x))
    y = Variable(torch.from_numpy(y))
    
    return (x, y)
    