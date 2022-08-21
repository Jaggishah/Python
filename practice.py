import pandas as pd

df = pd.read_excel('Book1.xlsx')
df
df.sort_values(by="id")
df