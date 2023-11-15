import matplotlib.pyplot as plt

wm_data = { "Brazil": {"titels": 5, "year": [1958, 1962, 1970, 1994, 2002]},
             "Germany":{"titels": 4, "year":[1954, 1974, 1990, 2014]},
             "Italy": {"titels": 4, "year":[1934, 1938, 1982, 2006]},
             "Argentina": {"titels": 3, "year":[1978, 1986, 2022]},
             "France": {"titels": 2, "year":[1998, 2018]},
             "Uruguay": {"titels": 2, "year":[1930, 1950]},
             "Spain": {"titels": 1, "year": [2010]} }

add_country = {"titels": 1, "year":[1966]}
wm_data["England"] = add_country

#extrair as chaves do dicionario 
countries = list(wm_data.keys())
titels = [country_data["titels"] for country_data in wm_data.values()]               # cria uma lista "title" onde cada elemento é o valor associado à chave "titles"
                                                                    
xlab = "Country"
ylab = "Titels"
title = "World Cup"

plt.title(title)
plt.xlabel(xlab)
plt.ylabel(ylab)
plt.grid(False)

for i, v in enumerate(titels):
    plt.text(i, v + 0.1, str(v), ha ="center", va = "bottom")

plt.bar(countries, height= titels, color = "blue")

plt.show()

print("Brazil hat " + str(wm_data["Brazil"]["titels"]) + " titels.")

