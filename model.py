import torch
from torch.autograd import Variable

class LinearRegession(torch.nn.Module):
    def __init__(self, input_size, output_size):
        super(LinearRegession, self).__init__()
        self.linear = torch.nn.Linear(input_size, output_size)
    
    def forward(self, x):
        out = self.linear(x)
        return out