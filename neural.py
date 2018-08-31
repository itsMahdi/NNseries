import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

n_nodes_hl1 = 500
n_nodes_hl1 = 500
n_nodes_hl1 = 500

n_classes = 10
batch_size = 100

# 28 * 28
x = tf.placeholder('float',[None , 784])
y = tf.placeholder('float')

def neural_networl_model(data):
    hidden_1_layer = {'weights':tf.Variable()}