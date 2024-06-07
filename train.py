import torch
from torch.autograd import Variable


def train(
        model,
        x_train,
        y_train,
        optimizer=torch.optim.SGD,
        criterion=torch.nn.MSELoss,
        epochs=100,
        lr=0.1
        ):
    optimizer = optimizer(model.parameters(), lr=lr)
    criterion = criterion()    

    for epoch in range(epochs):


        # Clearing gradient buffers because we don't want any gradient from previous epochs
        optimizer.zero_grad()

        # Get output from the model
        outputs = model(x_train)

        # Get loss for the predicted output
        loss = criterion(outputs, y_train)
        # print(f'loss : {loss}')

        # Get gradient w.r.t to parameters
        loss.backward()

        # Update parameters
        optimizer.step()
        print(f'epoch {epoch}, loss {loss}')
