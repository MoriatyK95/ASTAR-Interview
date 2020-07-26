#Author: Huakai Zeng
#Desrciption: ASTAR interview Q3, MLP with 3 inputs, 2 layers (each layer 4 nodes), 1 output
#incomplete, still trying to understand keras
#remarks: Having 16 digits accuracy, how many epochs will the network be able to predict

import numpy as np
import pandas as pd
import tensorflow as tf

if __name__ == '__main__':
    train_data = pd.read_table("train_data.txt")
    train_df = pd.DataFrame(train_data)
    truth_data = pd.read_table("train_truth.txt")
    train_truth_df = pd.DataFrame(truth_data)
    # print(truth_data.shape)
    data = pd.merge(train_df, train_truth_df, left_index=True, right_index=True)

    X = data[['x1', 'x2', 'x3']].to_numpy()
    Y = data[['y']].to_numpy()
    X = np.array(X)
    Y = np.array(Y)




    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Flatten())
    #4 nodes each layer
    model.add(tf.keras.layers.Dense(4, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(4, activation=tf.nn.relu))

    #1 output node
    model.add(tf.keras.layers.Dense(1, activation=tf.nn.elu))

    model.compile(optimizer= 'adam', loss='mean_squared_error', metrics=[tf.keras.metrics.Accuracy()])
    model.fit(X, Y, epochs= 100)



    prediction = model.predict(X)
    print(prediction)