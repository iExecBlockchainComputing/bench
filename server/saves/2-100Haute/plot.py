import json
import pandas as pd
import matplotlib.pyplot as plt

with open('2-100HauteFormatted.json') as f:
    d1 = json.load(f)

df1 = pd.DataFrame(d1)

ax1 = df1.plot(kind='scatter', label='122 noeuds', x='blockNumber', y='newStart', color='red')

ax1.set_xlabel("Numéro de bloc")
ax1.set_ylabel("Moment d'envoi d'une transaction (s)")
plt.show()
