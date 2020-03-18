import numpy as np
import pandas as pd


df = pd.DataFrame(np.random.rand(12).reshape(3,4)*100,
                  index = ['one','two','three'],
                  columns=['a','b','c'])

print(df)

