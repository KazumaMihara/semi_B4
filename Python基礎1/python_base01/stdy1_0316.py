#2021 03 16
import matplotlib.pyplot as plt
import numpy as np

def softmax(x):
    return np.exp(x) / sum(np.exp(x))

def tanh(x):
    ep = np.exp(x)
    en = np.exp(-x)
    return (ep - en) / (ep + en)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))


x = np.arange(-5.0, 5.0, 0.1)
y_soft = softmax(x)
y_sig = sigmoid(x)
y_tanh = tanh(x)

plt.title("sigmoid, softmax, tanh")
plt.xlabel("input")
plt.ylabel("output")

plt.plot(x,y_sig,label = 'sigmoid',color = 'green')
plt.plot(x,y_soft,label = 'softmax',color = 'red')
plt.plot(x,y_tanh,label = 'tanh',color = 'blue')

plt.xlim(-5.0,5.0)
plt.ylim(-1.5,1.5)
plt.grid()
plt.legend()
plt.show()
