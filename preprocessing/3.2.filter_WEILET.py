#https://habr.com/ru/post/451278/

import numpy as np
import matplotlib.pyplot as plt

import pywt
import pywt.data
import pandas as pd


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('not_alc_s2.csv')

df1=df["sensor value"]
df2=df["sensor position"]

FP1=[]
FP1_1=[]
FP2=[]
FP2_1=[]
for b in range (1,460):
 if df2[b]=="FP1":
  FP1.append(df1[b])
  FP1_1.append(df2[b])
 if df2[b]=="FP2":
  FP2.append(df1[b])
  FP2_1.append(df2[b])
 
df3 = pd.DataFrame(FP1, FP1_1)
df4 = pd.DataFrame(FP2, FP2_1)

plt.plot(FP2)
#plt.show()



import pywt
from pylab import *
from numpy import *
x = linspace (0,  1,  num = 2048)
y = FP2



import pywt
from pylab import *
from numpy import *

st='sym5'
(cA, cD) = pywt.dwt(y,st)
(cA, cD) = pywt.dwt(cA,st)
(cA, cD) = pywt.dwt(cA,st)
(cA, cD) = pywt.dwt(cA,st)
(cA, cD) = pywt.dwt(cA,st)

subplot(2, 1, 1)
plot(cA,'b',linewidth=2, label='cA,level-5')
grid()
legend(loc='best')
subplot(2, 1, 2)
plot(cD,'r',linewidth=2, label='cD,level-1')
grid()
legend(loc='best')
show()

