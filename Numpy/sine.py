#Sine wave plot tool
import numpy as np
import matplotlib.pyplot as plt

f = 0.5 # frequency of sine wave
A = 5 # maximum amplitude of sine wave

x = np.arange(-6.28, 6.28, 0.01) #set values from -pi to pi in 0.01 increments
y = A * np.tan( f * x )


plt.plot(x, y)

plt.title('sample plot')
plt.xlabel('angle')
plt.ylabel('amplitude')

plt.show()
