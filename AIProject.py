from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import numpy as np

# load pima indians dataset
dataset = np.loadtxt("https://raw.githubusercontent.com/badriadhikari/2019-Fall-AI/master/MODULE-I/pima-indians-diabetes.data.csv", delimiter=",")
print(dataset.shape)