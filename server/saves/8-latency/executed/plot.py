import json
import pandas as pd
import matplotlib.pyplot as plt

with open('results2.json') as f:
    d = json.load(f)

df = pd.DataFrame(d)

df.plot(kind='scatter', x='newStart', y='executionTime')
plt.show()
