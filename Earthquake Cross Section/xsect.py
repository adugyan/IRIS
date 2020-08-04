import os
import pandas as pd
import matplotlib.pyplot as plt

#Use the IRIS FetchEvent tool to download the hypocenters for a thin slice of earthquakes in the Oaxaca area of Mexico. I used longitude range restricted to between -94.5 and -94, while the latitude range would be from 14 to 19. Magnitudes greater than 4 should help to keep the location quality relatively high (smaller earthquakes are harder to locate because the signals are weaker)
os.system('FetchEvent --lon -94.5:-94 --lat 14:19 --mag 4:10 -o oaxaca.eve')

#stores the data from the file into variable df and outputs a few lines
df = pd.read_csv("oaxaca.eve",sep="|",header=None)
pd.set_option('display.max_columns', None)
print(df.head())

#plots using lat(index 2) as the x-axis and depth(4) as y.
plt.plot(df[2],df[4],'+')
plt.xlabel('Latitude')
plt.ylabel('Depth') 

plt.xlim(14.5,18)
plt.ylim(390,0)
plt.gca().xaxis.tick_top()
plt.gca().xaxis.set_label_position("top")
plt.show()
