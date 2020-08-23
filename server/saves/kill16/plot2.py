import json
import pandas as pd
import matplotlib.pyplot as plt

with open('7-32Kill16.json') as f:
    d1 = json.load(f)

df1 = pd.DataFrame(d1)

ax1 = df1.plot(kind='scatter', label='32 noeuds, 16 arrêts', x='executionTime', y='newStart', color='green')
ax1.set_xlabel("Temps d'exécution d'une transaction (s)")
ax1.set_ylabel("Moment d'envoie d'une transaction (s)")
plt.show()
