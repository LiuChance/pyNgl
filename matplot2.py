#引用部分
import numpy as np
import numpy as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

#数据准备
#pandas
#pd.dataframe:处理，操作结构化数据的利器

df = pd.read_csv('xwdata.csv')
df['资料时间']=pd.to_datetime(df['资料时间'])
df['站名']=pd.
t = np.array(df['资料时间'])

