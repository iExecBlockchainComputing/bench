import json
import pandas as pd
import matplotlib.pyplot as plt

with open('2-100HauteFormatted.json') as f:
    d1 = json.load(f)

with open('6-32HauteFormatted.json') as f:
    d2 = json.load(f)

df1 = pd.DataFrame(d1)
df2 = pd.DataFrame(d2)

ax1 = df1.plot(kind='scatter', label='122 noeuds', x='executionTime', y='newStart', color='red')
ax2 = df2.plot(kind='scatter', label='32 noeuds', x='executionTime', y='newStart', color='green')
# ax2.set_xlabel("Temps d'exécution d'une transaction (s)")
# ax2.set_ylabel("Moment d'envoie d'une transaction (s)")
plt.show()
