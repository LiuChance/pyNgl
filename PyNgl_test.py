import Nio
import numpy as np
import pandas as pd

print(Nio.__version__)
print(pd.__version__)

s = pd.Series(np.random.rand(5))
print(s)