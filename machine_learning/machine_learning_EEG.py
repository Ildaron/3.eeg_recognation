# S1 obj, S2 nomatch, S2 match
import numpy as np
import pandas as pd
data=pd.DataFrame()

for a in range (1,240):
 a=a+a
 adress = "Data"+str(a)+".csv"
 df = pd.read_csv(adress)
 df0= df['subject identifier'].map({'a': 1, 'c': 0})

 uniq=df["sensor position"].unique() 
 rep = dict(zip(uniq,range(len(uniq))))
 #print (rep)
 df["sensor position"]=df["sensor position"].map(rep)  # map he use dictionary bot without name
 df1=df["sensor position"]
 df2=df["sensor value"]
#df3=df["matching condition"]
 df3= df['matching condition'].map({'S1 obj': 0, 'S2 nomatch': 1, 'S2 match': 2})
 #df4=df["channel"]

 df5 = pd.DataFrame()
 df5['sensor position'] = df1
 df5['sensor value'] = df2
 df5['matching condition'] = df3

# df5['channel'] = df4
 df5['subject identifier'] = df0
 if a==1:
  #print ("a==1")
  data=df5
 if a>1:
  print (a)
  data=data.append(df5, ignore_index = True)

z=data.fillna(0)
print (z) 

from sklearn.model_selection import train_test_split
df = z.values
x = df[:,0:3]
y = df[:,3]                                                                                           
from sklearn import preprocessing
normalized_x = preprocessing.normalize(x) #
standardized_x = preprocessing.scale(x)   
print ("ok2")
                                                      # Feature Selection и Feature Engineering
from sklearn import metrics
from sklearn.ensemble import ExtraTreesClassifier
model = ExtraTreesClassifier()
model.fit(x, y)
#print(model.feature_importances_)
print ("ok3")
                                                     #Алгоритм перебора - Recursive Feature Elimination
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
# create the RFE model and select 3 attributes

rfe = RFE(model, 3)
rfe = rfe.fit(x, y)
                                        

from sklearn import metrics
from sklearn.svm import SVC
# fit a SVM model to the data
model = SVC()


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.7, random_state=42)
model.fit(x_train, y_train) 

#print(model)
#make predictions
expected = y_test
predicted = model.predict(x_test)

print ("ok5")
#summarize the fit of the model
#print(metrics.classification_report(expected, predicted))
#print(metrics.confusion_matrix(expected, predicted))

from sklearn.metrics import accuracy_score  
print(accuracy_score(y_test, predicted))   
