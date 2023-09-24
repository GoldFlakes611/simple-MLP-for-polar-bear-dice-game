# MLP for Polar bear around ice game
## Description:
The rules of this game is simple, a dice will be rolled 5 times, then the players will then guess how many polar bear, fish, and plankton there were. A table is used to calculate the number of polar bear, fish, and plankton. This project attempts to use a neural network to learn these mappings. Neural networks are universal function approximators and should in theory be able to learn simple mappings such as this one with relative ease. 

## Required libraries

- pytorch
- numpy
- pandas
- matplotlib
- scikit-learn

## Usage:
1. Run the dataset generator to create a dataset, the number of datapoints within the dataset can be adjusted. All of my testing were performed with 100 thousand data values. Run this script with
   
``` 
python dataset_generator.py
``` 
2. train.ipynb can then be used to train the MLP, hyperparameters have already been tuned with optuna. This script will save the model as model.pt
3. Hyperparameter_search.py can be used to tune the hyperparameters if desired. The number of trials will need to be adjusted based on the need, and computational resources. Run this script with 
``` 
python dataset_generator.py
```