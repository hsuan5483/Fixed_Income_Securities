# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 22:12:01 2019

@author: Pei-Hsuan Hsu

Email：amyhsu0619@gmail.com
"""
import os
from os.path import join
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

notional = 1e8
premium_rate = 0.025
pip = 0.0001
K = 0.01
spot = 1.35
currency = 'EURUSD'
#sim = pd.DataFrame(np.arange(spot-.03,spot+.03,0.0001), columns = [currency])
#sim['Swap Points'] = (1/sim[currency] - 1/spot)/pip
sim = pd.DataFrame(np.arange(-500,500,1), columns = ['Swap Points'])
sim[currency] = 1/(sim['Swap Points'] * pip + 1/spot)

cost = True
settle = []
for i in range(len(sim)):
    if sim['Swap Points'][i] > K:
        if cost:
            settle.append(notional * ((spot - sim[currency][i] + K) - premium_rate))
        else:
            settle.append(notional * (spot - sim[currency][i] + K))
    else:
        if cost:
            settle.append(-notional * premium_rate)
        else:
            settle.append(0)
    
sim['payoff'] = settle


# plot
fig, ax1 = plt.subplots()
#ax2 = ax1.twinx()

ax1.plot(sim['Swap Points'], sim['payoff'])
#ax2.plot(sim[currency], sim['Swap Points'])

plt.axhline(y=0, c = 'black')
#ax1.set_xlim(sim[currency][0])

ax1.set_xlabel('Swap Points (pips)', fontsize = 16)
ax1.set_ylabel('P/L (USD)', fontsize = 16)
ax1.set_title('Payoff', fontsize = 16)
#ax2.set_ylabel('Swap Points', fontsize = 16)
#plt.savefig('matplotlib_horizontal_line_03.png', bbox_inches='tight')
plt.show()
