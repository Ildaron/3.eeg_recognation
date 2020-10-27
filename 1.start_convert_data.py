import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

df = pd.read_csv('4.not_alc_s2.csv')


df1=df["sensor value"]
df2=df["sensor position"]
df3=df["sample num"]

FP1=[]
FP1_1=[]
FP2=[]
FP2_1=[]
F7=[]
F7_1=[]
F8=[]
F8_1=[]
AF1=[]
AF1_1=[]
AF2=[]
AF2_1=[]
FZ1=[]
FZ1_1=[]
F4=[]
F4_1=[]
F3=[]
F3_1=[]
FC6=[]
FC6_1=[]
FC5=[]
FC5_1=[]
FC2=[]
FC2_1=[]
FC1=[]
FC1_1=[]
T8=[]
T8_1=[]
T7=[]
T7_1=[]
CZ=[]
CZ1=[]
C3=[]
C3_1=[]
C4=[]
C4_1=[]
CP5=[]
CP5_1=[]
CP6=[]
CP6_1=[]
CP1=[]
CP1_1=[]
CP2=[]
CP2_1=[]
P3=[]
P3_1=[]
P4=[]
P4_1=[]
PZ=[]
PZ_1=[]
P8=[]
P8_1=[]
P7=[]
P7_1=[]
PO2=[]
PO2_1=[]
PO1=[]
PO1_1=[]
O2=[]
O2_1=[]
O1=[]
O1_1=[]
X=[]
X_1=[]
AF7=[]
AF7_1=[]
AF8=[]
AF8_1=[]
F5=[]
F5_1=[]
F6=[]
F6_1=[]
FT7=[]
FT7_1=[]
FT8=[]
FT8_1=[]
FPZ=[]
FPZ_1=[]

FC4=[]
FC4_1=[]

FC3=[]
FC3_1=[]
C6=[]
C6_1=[]
C5=[]
C5_1=[]
F2=[]
F2_1=[]
F1=[]
F1_1=[]
TP8=[]
TP8_1=[]
TP7=[]
TP7_1=[]
AFZ=[]
AFZ_1=[]
CP3=[]
CP3_1=[]
CP4=[]
CP4_1=[]
P5=[]
P5_1=[]
P6=[]
P6_1=[]
C1=[]
C1_1=[]
C2=[]
C2_1=[]

PO7=[]
PO7_1=[]
PO8=[]
PO8_1=[]
FCZ=[]
FCZ_1=[]
POZ=[]
POZ_1=[]
OZ=[]
OZ_1=[]
P2=[]
P2_1=[]
P1=[]
P1_1=[]
CPZ=[]
CPZ_1=[]
nd=[]
nd_1=[]
Y=[]
Y_1=[]

s=[]




print ("ok")
i=1


for b in range (0,16384):
 if df2[b]=="FP1":
  FP1.append(df1[b])
  FP1_1.append(df2[b])
  s.append(i)
  
 if df2[b]=="FP2":
  FP2.append(df1[b])
  FP2_1.append(df2[b])

 if df2[b]=="F7":
  F7.append(df1[b])
  F7_1.append(df2[b])


 if df2[b]=="F8":
  F8.append(df1[b])
  F8_1.append(df2[b])
  #print("works")

 if df2[b]=="AF1":
  AF1.append(df1[b])
  AF1_1.append(df2[b])

 if df2[b]=="AF2":
  AF2.append(df1[b])
  AF2_1.append(df2[b])

 if df2[b]=="FZ":
  FZ1.append(df1[b])
  FZ1_1.append(df2[b])

 if df2[b]=="F4":
  F4.append(df1[b])
  F4_1.append(df2[b])

 if df2[b]=="F3":
  F3.append(df1[b])
  F3_1.append(df2[b])

 if df2[b]=="FC1":
  FC6.append(df1[b])
  FC6_1.append(df2[b])  

 if df2[b]=="FC5":
  FC5.append(df1[b])
  FC5_1.append(df2[b])  

 if df2[b]=="FC2":
  FC2.append(df1[b])
  FC2_1.append(df2[b])


 if df2[b]=="FC1":
  FC1.append(df1[b])
  FC1_1.append(df2[b])

 if df2[b]=="T8":
  T8.append(df1[b])
  T8_1.append(df2[b])

 if df2[b]=="T7":
  T7.append(df1[b])
  T7_1.append(df2[b])

 if df2[b]=="CZ":
  CZ.append(df1[b])
  CZ1.append(df2[b])

 if df2[b]=="C3":
  C3.append(df1[b])
  C3_1.append(df2[b])  

 if df2[b]=="C4":
  C4.append(df1[b])
  C4_1.append(df2[b])  

 if df2[b]=="CP5":
  CP5.append(df1[b])
  CP5_1.append(df2[b])  

 if df2[b]=="CP6":
  CP6.append(df1[b])
  CP6_1.append(df2[b])

 if df2[b]=="CP1":
  CP1.append(df1[b])
  CP1_1.append(df2[b])

 if df2[b]=="CP2":
  CP2.append(df1[b])
  CP2_1.append(df2[b])
  
 if df2[b]=="P3":
  P3.append(df1[b])
  P3_1.append(df2[b])

 if df2[b]=="P4":
  P4.append(df1[b])
  P4_1.append(df2[b])

 if df2[b]=="PZ":
  PZ.append(df1[b])
  PZ_1.append(df2[b])

 if df2[b]=="P8":
  P8.append(df1[b])
  P8_1.append(df2[b])

 if df2[b]=="P7":
  P7.append(df1[b])
  P7_1.append(df2[b])

 if df2[b]=="PO2":
  PO2.append(df1[b])
  PO2_1.append(df2[b])

 if df2[b]=="PO1":
  PO1.append(df1[b])
  PO1_1.append(df2[b])

 if df2[b]=="O2":
  O2.append(df1[b])
  O2_1.append(df2[b])

 if df2[b]=="O1":
  O1.append(df1[b])
  O1_1.append(df2[b])

 if df2[b]=="X":
  X.append(df1[b])
  X_1.append(df2[b])

 if df2[b]=="AF7":
  AF7.append(df1[b])
  AF7_1.append(df2[b])

 if df2[b]=="AF8":
  AF8.append(df1[b])
  AF8_1.append(df2[b])

 if df2[b]=="F5":
  F5.append(df1[b])
  F5_1.append(df2[b])

 if df2[b]=="F6":
  F6.append(df1[b])
  F6_1.append(df2[b])

 if df2[b]=="FT7":
  FT7.append(df1[b])
  F7_1.append(df2[b])

 if df2[b]=="FT8":
  FT8.append(df1[b])
  F8_1.append(df2[b])

 if df2[b]=="FPZ":
  FPZ.append(df1[b])
  FPZ_1.append(df2[b])

 if df2[b]=="FC4":
  FC4.append(df1[b])
  FC4_1.append(df2[b])

 if df2[b]=="FC3":
  FC3.append(df1[b])
  FC3_1.append(df2[b])

 if df2[b]=="C6":
  C6.append(df1[b])
  C6_1.append(df2[b])

 if df2[b]=="C5":
  C5.append(df1[b])
  C5_1.append(df2[b])

 if df2[b]=="F2":
  F2.append(df1[b])
  F2_1.append(df2[b])


 if df2[b]=="F1":
  F1.append(df1[b])
  F1_1.append(df2[b])


 if df2[b]=="TP8":
  TP8.append(df1[b])
  TP8_1.append(df2[b])

 if df2[b]=="TP7":
  TP7.append(df1[b])
  TP7_1.append(df2[b])

 if df2[b]=="AFZ":
  AFZ.append(df1[b])
  AFZ_1.append(df2[b])


 if df2[b]=="CP3":
  CP3.append(df1[b])
  CP3_1.append(df2[b])

 if df2[b]=="CP4":
  CP4.append(df1[b])
  CP4_1.append(df2[b])

 if df2[b]=="P5":
  P5.append(df1[b])
  P5_1.append(df2[b])

 if df2[b]=="P6":
  P6.append(df1[b])
  P6_1.append(df2[b])


 if df2[b]=="C1":
  C1.append(df1[b])
  C1_1.append(df2[b])


 if df2[b]=="C2":
  C2.append(df1[b])
  C2_1.append(df2[b])

 if df2[b]=="PO7":
  PO7.append(df1[b])
  PO7_1.append(df2[b])


 if df2[b]=="PO8":
  PO8.append(df1[b])
  PO8_1.append(df2[b])

 if df2[b]=="FCZ":
  FCZ.append(df1[b])
  FCZ_1.append(df2[b])


 if df2[b]=="POZ":
  POZ.append(df1[b])
  POZ_1.append(df2[b])

 if df2[b]=="OZ":
  OZ.append(df1[b])
  OZ_1.append(df2[b])

 if df2[b]=="P2":
  P2.append(df1[b])
  P2_1.append(df2[b])

 if df2[b]=="P1":
  P1.append(df1[b])
  P1_1.append(df2[b])

 if df2[b]=="CPZ":
  CPZ.append(df1[b])
  CPZ_1.append(df2[b])

 if df2[b]=="nd":
  nd.append(df1[b])
  nd_1.append(df2[b])


 if df2[b]=="Y":
  Y.append(df1[b])
  Y_1.append(df2[b])


print ("check")

df4 = pd.DataFrame(s)
df4['C'] = FP1
df4['C1'] = FP2
df4['C2'] = F7

df4['C3'] = F8
print ("check1")

df4['C4'] = AF1
df4['C5'] = AF2
df4['C6'] = FZ1
df4['C7'] = F4
df4['C8'] = F3
df4['C9'] = FC6
df4['C10'] = FC5
df4['C11'] = FC2
df4['C12'] = FC1
df4['C13'] = T8
df4['C14'] = T7
df4['C15'] = CZ
df4['C16'] = C3
df4['C17'] = C4
df4['C18'] = CP5
df4['C19'] = CP6
df4['C20'] = CP1
df4['C21'] = CP2
df4['C22'] = P3
print ("check2")

#df4['C1'] = z
df4['C23'] = P4
df4['C24'] = PZ
df4['C25'] = P8
df4['C26'] = P7
df4['C27'] = PO2
df4['C28'] = PO1
df4['C29'] = O2
df4['C30'] = O1
df4['C31'] = X
df4['C32'] = AF7
df4['C33'] = AF8
df4['C34'] = F5
df4['C35'] = F6
df4['C36'] = FT7
df4['C37'] = FT8
df4['C38'] = FPZ
df4['C39'] = FC4
df4['C40'] = FC3
df4['C41'] = C6
print ("check3")

df4['C42'] = C5
df4['C43'] = F2
df4['C44'] = F1
df4['C45'] = TP8
df4['C46'] = TP7
df4['C47'] = AFZ
df4['C48'] = CP3
df4['C49'] = CP4
df4['C50'] = P5
df4['C51'] = P6
df4['C52'] = C1
print ("check6")


df4['C53'] = C2
df4['C54'] = PO7
df4['C55'] = PO8
df4['C56'] = FCZ
df4['C57'] = POZ
df4['C58'] = OZ
df4['C59'] = P2
df4['C60'] = P1
print ("check4")
df4['C61'] = CPZ
df4['C62'] = nd
print ("check5")
#df4['C63'] = Y

print (df4)


df4.to_csv("8.not_alc_s2_conv.csv")



