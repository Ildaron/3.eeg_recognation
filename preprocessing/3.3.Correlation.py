import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#df = pd.read_csv('C:/Users/Leisan/Desktop/science/12.Brain/4/Data1.csv')
df4 = pd.read_csv('not_alc_s2_conv.csv')

#print (df4)
corr_matrix=df4.values

#fig_cor, axes_cor = plt.subplots()
fig_cor, axes_cor = plt.subplots(1, sharex=True, figsize=(50,100))
#print (fig_cor)
#print (axes_cor)
#print (plt.subplots(1,1))

fig_cor.set_size_inches(6, 6)

x=[]
for b in range (0,256):
 x.append(b)
#print (a)
labels_x = x

y=[]
for b in range (0,63):
 y.append(b)
#print (a)
labels_y = y

myimage = axes_cor.imshow(corr_matrix)
plt.colorbar(myimage)

axes_cor.set_yticks(np.arange(0,corr_matrix.shape[0], corr_matrix.shape[0]*1.0/len(labels_x)))
axes_cor.set_xticks(np.arange(0,corr_matrix.shape[1], corr_matrix.shape[1]*1.0/len(labels_y)))

#print (np.arange(0,corr_matrix.shape[0], corr_matrix.shape[0]*1.0/len(labels_y)))
#print(np.arange(0,corr_matrix.shape[1], corr_matrix.shape[1]*1.0/len(labels_x)))

axes_cor.set_yticklabels(labels_x)
axes_cor.set_xticklabels(labels_y)

#plt.draw()
plt.tight_layout()
plt.show()
