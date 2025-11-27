import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

end = pd.read_csv('sample_11.2_6/C3-100/_015.txt', skiprows=4)

fig, ax = plt.subplots(ncols=1, nrows=2, figsize = [10, 8])

ax[0].plot(end['Endurance: Time'], end['Voltage'])
ax[1].plot(end['Endurance: Time'], (end['Current']))

plt.show()