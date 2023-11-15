import matplotlib.pyplot as plt

countries = ["Brasilien", "Deutschland", "Italien", "Argentinien", "Frankreich", "Uruguai", "Spanien"]
titles = [5, 4, 4, 3, 2, 2, 1]

countries = countries+ ["England"] 
titles = titles + [1] 


xlab = "Land"
ylab = "Titel"
title = "World Cup"

#plt.plot(länder, meisterschaft)   # nicht gut dafür  ////   #plt.scatter(länder, meisterschaft)   # auch nicht optimal

plt.title(title)
plt.xlabel(xlab)
plt.ylabel(ylab)
plt.grid(False)

for i, v in enumerate(titles):
    plt.text(i, v + 0.1, str(v), ha ="center", va = "bottom")



plt.bar(countries, titles, color = "blue" )
plt.show()