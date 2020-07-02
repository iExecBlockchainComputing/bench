import json
import pandas as pd
import matplotlib.pyplot as plt

with open('blocknum.json') as f:
    d = json.load(f)

df = pd.DataFrame(d)

df.plot(kind='scatter', x='start', y='blockNumber')
plt.show()