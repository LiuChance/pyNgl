#引用部分
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

#数据准备
#pandas
#pd.dataframe:处理，操作结构化数据的利器

df = pd.read_csv('data/57044.csv')
df['Datetime']=pd.to_datetime(df['Datetime'])
t = [datetime.strptime(d, '%Y-%m-%d %H:%M:%s') for d in df['Datetime']]
tmp = np.array(df['TEM'])
prs = np.array(df['PRS'])
rhu = np.array(df['RHU'])
print(t)