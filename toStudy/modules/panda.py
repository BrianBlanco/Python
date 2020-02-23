# Data
dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

# Impor package pandas
import pandas as pd

# Format the data into columns
brics = pd.DataFrame(dict)
# Set the index for brics
brics.index = ["BR", "RU", "IN", "CH", "SA"]

print(brics)
