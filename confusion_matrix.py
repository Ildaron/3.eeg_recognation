import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

y1 =    [1,1,1]
y1_n = [1,1,1,]

y2      = [1,1,1,1,1,1,1,1,1,1,1,1,1]               
y2_n = [0,0,0,0,0,0,0,0,0,0,0,0,0]

y3 =    [0,0,0]
y3_n =  [1,1,1]

y4 =[0,0,0]
y4_n = [1,1,1]  

y_actual= y1+ y2 + y3  + y4
y_predict=y1_n+y2_n +y3_n +y4_n

print (len(y_actual))
data = {'y_Actual': y_actual,
        'y_Predicted': y_predict
        }
df = pd.DataFrame(data, columns=['y_Actual','y_Predicted'])
confusion_matrix = pd.crosstab(df['y_Actual'], df['y_Predicted'], rownames=['Actual'], colnames=['Predicted'])

sn.heatmap(confusion_matrix, annot=True)
plt.show()
