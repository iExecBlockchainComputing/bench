import json
import pandas as pd
import matplotlib.pyplot as plt

with open('1-100BasseFormatted.json') as f:
    d1 = json.load(f)

with open('3-62BasseFormatted.json') as f:
    d2 = json.load(f)

with open('5-32BasseFormatted.json') as f:
    d3 = json.load(f)

df1 = pd.DataFrame(d1)
df2 = pd.DataFrame(d2)
df3 = pd.DataFrame(d3)

ax1 = df1.plot(kind='scatter', label='122 noeuds', x='executionTime', y='newStart', color='red', s=2)
ax2 = df2.plot(ax=ax1, kind='scatter', label='62 noeuds', x='executionTime', y='newStart', color='orange', s=2)
ax3 = df3.plot(ax=ax2, kind='scatter', label='32 noeuds', x='executionTime', y='newStart', color='green', s=2)
ax3.set_xlabel("Temps d'exécution d'une transaction (s)")
ax3.set_ylabel("Moment d'envoie d'une transaction (s)")
plt.show()
