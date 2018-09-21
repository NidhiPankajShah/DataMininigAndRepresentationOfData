import pandas as pd
import xlrd
import matplotlib.pyplot as plt
from matplotlib import  style

style.use('fivethirtyeight')

country = pd.read_excel('C:\\Users\\Public\\dataset.xlsx')
df = country.head(48)
df = df.set_index(["Country"])
sd = df.reindex(columns=['Unemployment_rate_rural','Unemployment_rate_urban'])
print(sd)
sd.plot()
plt.show()

sd1 = df.reindex(columns=['Median_income_rural','median_income_urban'])
print(sd1)
sd1.plot()
plt.show()
