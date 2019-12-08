import matplotlib.pyplot as plt
import numpy as np

def plot(n):
    if n<=9:
        return n*n-7
    else:
        return (n-10)*(n-10)-7
yaxis = np.vectorize(plot)
x=np.arange(0,100)
y=yaxis(x)
plt.axis([0,100,-411,10000])
plt.stem(x,y)
plt.show()