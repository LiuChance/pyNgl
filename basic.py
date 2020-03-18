
#绘制y=x2曲线

#引用部分
import numpy as np
import matplotlib.pyplot as plt

#数据准备
x = np.arange(-5, 6, 1)
y = x**2  #y = pow(x,2)

#绘制部分
fig = plt.figure(figsize=(9,5),dpi=100)
plt.plot(x,y,'kh-.',label='$y=x^2$')
plt.legend(loc=9)
plt.title('$y=x^2$')

plt.savefig('FirstPic.png')
plt.show()

