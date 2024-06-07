import numpy as np
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

def plot_validation(x, y, y_pred):
    fig = plt.figure(figsize=(12,8))
    plt.scatter(x.detach().numpy(), y.detach().numpy(), color='blue')
    plt.plot(x.detach().numpy(), y_pred.detach().numpy(), color='red')
    plt.show()

