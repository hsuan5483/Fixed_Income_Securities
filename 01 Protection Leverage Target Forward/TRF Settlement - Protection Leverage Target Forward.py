# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 23:45:58 2019

@author: Pei-Hsuan Hsu

Email：amyhsu0619@gmail.com
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

currency = 'EUR/USD'
notional = 1000000
Target = 0.1
spot = 1.375
Barrier = 1.435
K = 1.415
L = 2
PL = 1
args = [Target, Barrier, K, L, PL]

sim = pd.DataFrame(np.arange(K-Target-.01,K+0.05,0.0001), columns = [currency])

settle = []
for i in range(len(sim)):
    if sim[currency][i] <= K - Target:
        settle.append(notional*(Target))
    
    elif sim[currency][i] <= K:
        settle.append(notional*(K - sim[currency][i]))
    
    elif K < sim[currency][i] <= Barrier:
        settle.append(notional*PL*(K - sim[currency][i]))
        
    else:
        settle.append(notional*L*(K - sim[currency][i]))

sim['payoff'] = settle

# plot
fig, ax = plt.subplots()

plt.plot(sim[currency], sim['payoff'])
plt.axhline(y=0, c = 'black')

ax.scatter([spot, K, Barrier], [0,0,0], c = 'r')
ax.scatter([K, Barrier], [0,0], c = 'y')

ax.set_xlim(sim[currency][0])

ax.set_xlabel('Fixing Rate', fontsize = 16)
ax.set_ylabel('P/L', fontsize = 16)
ax.set_title('Payoff', fontsize = 16)

#plt.savefig('matplotlib_horizontal_line_03.png', bbox_inches='tight')
plt.show()
