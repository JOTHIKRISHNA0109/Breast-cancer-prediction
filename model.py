import main.py
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

#Building the neural network with three layers where one input, one hidden and
# one output layer with softmax function 
l1=tf.keras.layers.Dense(units=10,input_shape=[10])
l2=tf.keras.layers.Dense(units=5,activation='relu')
l3=tf.keras.layers.Dense(units=2,activation='softmax')
class_model=tf.keras.Sequential([l1,l2,l3])

#Compilation of the model with respective loss and metrics
class_model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(),
              metrics=['accuracy'])

#Training the model with training data
class_model.fit(X_train,Y_train,epochs=100,validation_split=0.2,verbose=1)

#Evaluating the model with test data
class_model.evaluate(X_test,Y_test)
