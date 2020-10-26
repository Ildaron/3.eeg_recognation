
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('1.alc_s1.csv')
df1=df["sensor value"]
df2=df["sensor position"]

FP1=[]
FP1_1=[]
FP2=[]
FP2_1=[]
s=[]
a=1
for b in range (1,460):
 if df2[b]=="FP1":
  FP1.append(df1[b])
  FP1_1.append(df2[b])
 if df2[b]=="FP2":
  FP2.append(df1[b])
  FP2_1.append(df2[b])
  s.append(b)
#plt.plot(FP2)

# Python example - Fourier transform using numpy.fft method
import numpy as np
import matplotlib.pyplot as plotter
# How many time points are needed i,e., Sampling Frequency
samplingFrequency   = 204;
# At what intervals time points are sampled
samplingInterval = 1 / samplingFrequency;
# Begin time period of the signals
beginTime           = 0;
# End time period of the signals
endTime             = 1; 
# Frequency of the signals
signal1Frequency     = 4;
signal2Frequency     = 7;
# Time points
time        = np.arange(beginTime, endTime, samplingInterval);
# Create two sine waves

amplitude1 = FP2
amplitude2 = np.sin(2*np.pi*signal2Frequency*time)
# Create subplot
figure, axis = plotter.subplots(4, 1)
plotter.subplots_adjust(hspace=1)
# Time domain representation for sine wave 1
axis[0].set_title('Sine wave with a frequency of 4 Hz')
axis[0].plot(time, amplitude1)
axis[0].set_xlabel('Time')
axis[0].set_ylabel('Amplitude')
# Time domain representation for sine wave 2
axis[1].set_title('Sine wave with a frequency of 7 Hz')
axis[1].plot(time, amplitude2)
axis[1].set_xlabel('Time')
axis[1].set_ylabel('Amplitude')
# Add the sine waves
amplitude = amplitude1 + amplitude2
# Time domain representation of the resultant sine wave
axis[2].set_title('Sine wave with multiple frequencies')
axis[2].plot(time, amplitude)
axis[2].set_xlabel('Time')
axis[2].set_ylabel('Amplitude')
# Frequency domain representation
fourierTransform = np.fft.fft(amplitude)/len(amplitude)           # Normalize amplitude
fourierTransform = fourierTransform[range(int(len(amplitude)/2))] # Exclude sampling frequency
tpCount     = len(amplitude)
values      = np.arange(int(tpCount/2))
timePeriod  = tpCount/samplingFrequency
frequencies = values/timePeriod
# Frequency domain representation
axis[3].set_title('Fourier transform depicting the frequency components')
axis[3].plot(frequencies, abs(fourierTransform))
axis[3].set_xlabel('Frequency')
axis[3].set_ylabel('Amplitude')

plotter.show()
