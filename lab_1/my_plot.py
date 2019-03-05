from numpy import *
from numpy.random import *
from matplotlib.pyplot import *

def char(x):
    t = np.arange(0., x, 0.1)
    plot(t,sin(t), 'r-')
    show()
char(20)