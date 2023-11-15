import matplotlib.pyplot as plt

wm_data = { "Brasilien": {"titels": 5},
             "Deutschland":{"titels": 4},
             "Italien": {"titels": 4},
             "Argentinien": {"titels": 3},
             "Frankreich": {"titels": 2},
             "Uruguai": {"titels": 2},
             "Spanien": {"titels": 1} }

add_country = {"titels": 1}
wm_data["England"] = add_country

#extrair as chaves do dicionario 
countries = list(wm_data.keys())
titels = [country_data["titels"] for country_data in wm_data.values()]               # cria uma lista "title" onde cada elemento é o valor associado à chave "titles"
                                                                    
xlab = "Land"
ylab = "Titels"
title = "Fußball Weltmeisterschaft"

plt.title(title)
plt.xlabel(xlab)
plt.ylabel(ylab)
plt.grid(False)

plt.bar(countries, height= titels, color = "blue")

plt.show()

print("Brasilien hat " + str(wm_data["Brasilien"]["titels"]) + " titels")

