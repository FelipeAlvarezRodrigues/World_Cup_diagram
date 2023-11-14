import matplotlib.pyplot as plt
import numpy as np

länder = ["brasilien", "deutschland", "italien", "argentinien", "frankreich", "uruguai", "spanien"]
meisterschaft = [5, 4, 4, 3, 2, 2, 1]


xlab = "Land"
ylab = "Titel"
title = "Fußball-Weltmeisterschaft"

länder = ["england"] + länder
meisterschaft = [1] + meisterschaft

np_länder = np.array(länder)
np_meisterschaft = np.array(meisterschaft)

#plt.plot(länder, meisterschaft)   # nicht gut dafür
#plt.scatter(länder, meisterschaft)   # auch nicht optimal

plt.title(title)
plt.xlabel(xlab)
plt.ylabel(ylab)
plt.grid(True)


plt.hist(länder)
plt.show()