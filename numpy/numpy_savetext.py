# Import the numpy package as np
import numpy as np

x = np.arange(0.0,5.0,1.0)
np.savetxt('test.out', x, delimiter=',')