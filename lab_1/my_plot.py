from numpy import *
from numpy.random import *
from matplotlib.pyplot import *

t = np.arange(0., 20., 0.1)
plot(t,sin(t), 'r-')
show()