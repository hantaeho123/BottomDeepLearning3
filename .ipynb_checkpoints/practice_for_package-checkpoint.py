import dezero.core_simple as core_simple
import numpy as np

x = core_simple.Variable(np.array(2.0))
y = x ** 2 + 3 * x + 4

print(x)