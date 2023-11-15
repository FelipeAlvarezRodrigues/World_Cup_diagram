import matplotlib.pyplot as plt

länder = ["Brasilien", "Deutschland", "Italien", "Argentinien", "Frankreich", "Uruguai", "Spanien"]
meisterschaft = [5, 4, 4, 3, 2, 2, 1]

länder = länder + ["England"] 
meisterschaft = meisterschaft + [1] 


xlab = "Land"
ylab = "Titel"
title = "Fußball-Weltmeisterschaft"

#plt.plot(länder, meisterschaft)   # nicht gut dafür  ////   #plt.scatter(länder, meisterschaft)   # auch nicht optimal

plt.title(title)
plt.xlabel(xlab)
plt.ylabel(ylab)
plt.grid(False)

for i, v in enumerate(meisterschaft):
    plt.text(i, v + 0.1, str(v), ha ="center", va = "bottom")



plt.bar(länder, meisterschaft, color = "blue" )
plt.show()