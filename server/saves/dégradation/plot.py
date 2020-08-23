import json
import pandas as pd
import matplotlib.pyplot as plt

with open('12-debitHaut.json') as f:
    d1 = json.load(f)

with open('9-debitBas.json') as f:
    d2 = json.load(f)

df1 = pd.DataFrame(d1)
df2 = pd.DataFrame(d2)

ax1 = df1.plot(kind='scatter', label='32 noeuds, débit haut', x='blockNumber', y='newStart', color='green')
ax2 = df2.plot(ax=ax1, kind='scatter', label='32 noeuds, débit bas', x='blockNumber', y='newStart', color='red')

ax1.set_xlabel("Numéro de bloc")
ax2.set_ylabel("Moment d'envoi d'une transaction (s)")
plt.show()
