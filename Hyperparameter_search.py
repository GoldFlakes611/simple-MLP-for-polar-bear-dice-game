import torch
import pandas as pd
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
import optuna

if torch.cuda.is_available():
    device = torch.device("cuda")

#read the dataset
dataset = pd.read_csv("output.csv")
dataset=dataset.drop(dataset.columns[[0]], axis=1)
X = dataset.iloc[:, 0:5].values
Y = dataset.iloc[:, 5:].values

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)
x_train, y_train, x_test, y_test = (
    torch.tensor(x_train, dtype=torch.float32,device=device),
    torch.tensor(y_train, dtype=torch.float32,device=device),
    torch.tensor(x_test, dtype=torch.float32,device=device),
    torch.tensor(y_test, dtype=torch.float32,device=device))

#build the neural network
class PolarBear(nn.Module):
    def __init__(self, l1):
        super().__init__()
        self.l1 = l1
        self.input = nn.Linear(5, l1)
        self.input_act = nn.ReLU()
        self.output = nn.Linear(l1,3)
    def forward(self,x):
        x = self.input_act(self.input(x))
        x = self.output(x)
        return x
def train(model,n_epoch,lr,batch_size):
    loss_fn = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=lr)
    losses = []
    for epoch in range(n_epoch):
        for i in range(0,len(x_train),batch_size):
            Xbatch = x_train[i:i+batch_size]
            Ybatch = y_train[i:i+batch_size]
            y_pred = model(Xbatch)
            loss = loss_fn(y_pred, Ybatch)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        losses.append(float(loss))
    return model, loss

def objective(trial):
    l1 = trial.suggest_int('l1',30, 150)
    lr = trial.suggest_float('lr', 0.000001, 0.1, log=True)
    model = PolarBear(l1=l1)
    model.to(device)
    model, loss = train(model,30000,lr,80000)
    return loss


study = optuna.create_study(direction='minimize')
study.optimize(objective, n_trials=600)

print(optuna.trial.Trial.number)