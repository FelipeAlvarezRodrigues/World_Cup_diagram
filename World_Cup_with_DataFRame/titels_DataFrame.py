dict = { 
    "country":["Brasilien", "Deutschland", "Italien", "Argentinien", "Frankreich", "Uruguai", "Spanien", "England"],
    "titels": [5, 4, 4, 3, 2, 2, 1, 1],
    "year":[[1958, 1962, 1970, 1994, 2002], [1954, 1974, 1990, 2014], [1934, 1938, 1982, 2006], [1978, 1986, 2022], [1998, 2018], [1930, 1950], [2010], [1966]]
}

import pandas as pd

wm_data = pd.DataFrame(dict)
print(wm_data)

# wm_data.to_csv("wm_data.csv", index=False)           #---> csv datei erstellen(ohne index)

