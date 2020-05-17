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
upfront = 50000
TG = 0.1
TGC = 4
spot = 1.375
K = 1.335
L = 2

sim = pd.DataFrame(np.arange(K-.11,K+0.1,0.0001), columns = [currency])

settle1 = []
for i in range(len(sim)):
  
    if sim[currency][i] < K - TG:
        settle1.append(notional*(TG))
    
    elif sim[currency][i] < K:
        settle1.append(notional*(K - sim[currency][i]))
    
    else:
        settle1.append(notional*L*(K - sim[currency][i]))

sim['payoff1'] = settle1

# event1 occured before event2 
settle2 = []
for i in range(len(sim)):
    
#    if sim[currency][i] < K:
#        settle2.append(notional*(TG))
    
    if sim[currency][i] < K:
        settle2.append(notional*(K - sim[currency][i]))
    
    else:
        settle2.append(notional*L*(K - sim[currency][i]))

sim['payoff2'] = settle2


# plot
fig, ax = plt.subplots()

#plt.plot(sim[currency], sim['payoff2'], c='#5DADE2', label = "E1 and E2 didn't occur")
plt.plot(sim[currency], sim['payoff1'], c='#F5B041')#, label = 'E2 or E1 occured'

plt.axhline(y=0, c = 'black')

ax.scatter([spot, K], [0,0], c = 'r')
ax.scatter([K, K-TG], [0, 0], c = 'y')

ax.set_xlim(sim[currency][0])

#ax.legend()

ax.set_xlabel('Fixing Rate', fontsize = 16)
ax.set_ylabel('P/L', fontsize = 16)
ax.set_title('Payoff', fontsize = 16)

#plt.savefig('matplotlib_horizontal_line_03.png', bbox_inches='tight')
plt.show()
