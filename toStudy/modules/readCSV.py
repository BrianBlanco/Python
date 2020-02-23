

# Impor package pandas
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv(
    "C:\\Users\\Brian\\Desktop\\github\\Python\\toStudy\\modules\\cars.csv",
    names=["Nombre", "Edad", "waer"],
)

# Print out cars
print(cars.iloc[2])
