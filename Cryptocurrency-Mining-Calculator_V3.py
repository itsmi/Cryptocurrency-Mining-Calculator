from __future__ import division

# -*- coding: utf-8 -*-
"""

Cryptocurrency-Mining-Calculator

Computes optimized reinvestment rates for maximum return on investment for providers, auch as Genesis and Hashflare mining.

@author: Jochen Mueller

"""

' ################################# '
' Packages '
' ################################# '

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

' ################################# '
' Parameters '
' ################################# '

init_invest = 550 # USD
init_hashpwr_price = 0.22 # USD / GH/s
invest_dur = 2 * 365 # days
hashpwr_dur = 365 # days
BTC_price = 11000 # USD
BTC_return = 0.00000012 # BTC per day and GH/s
eff_red = 0.4 # relative effective reduction in efficiency per year. Calculated as: 1-eff_red. Therefore: 0: no change; 1: complete shutdown
hashpwr_price_red = 0.3 # relative reduction in cost of hashpower per year. Calculated as: 1-hashpwr_price_red. Therefore: 0: no change; 1: free; negativ: increase in price

' ################################# '
' Calculations '
' ################################# '

def calculations(opt_reinvest,init_invest,init_hashpwr_price,invest_dur,hashpwr_dur,BTC_price,BTC_return,eff_red,hashpwr_price_red):
    """ Calculates the data structure with all important values for the optimization """
    
    init_hashpwr = init_invest / init_hashpwr_price # GH/s
    data = np.zeros((invest_dur+hashpwr_dur,7))
    data[0,0] = 1 # day
    data[0:hashpwr_dur,1] = init_hashpwr # available hashpwr
    data[0,2] = 0 # return in USD
    data[0,4] = 0 # USD taken out per day
    data[0,5] = 0 # USD taken out accumulated
    data[0,6] = 0 # hashrate bought
    
    # Define reinvest rate for each day
    data[0:len(opt_reinvest),3] = opt_reinvest
    
    # Other calculations
    for i in range(1, invest_dur):
        data[i,0] = i+1 # day
        data[i:i+hashpwr_dur,1] = data[i:i+hashpwr_dur,1] + data[i-1,6] # available hashpwr
        data[i,2] = data[i,1] * BTC_return * (1-eff_red)**(i/365) * BTC_price # return in USD
        data[i,4] = data[i,2] * (1-data[i,3]) # USD taken out per day
        data[i,5] = data[i-1,5] + data[i,4] # USD taken out accumulated
        data[i,6] = data[i,2] * data[i,3] / (init_hashpwr_price * (1-hashpwr_price_red)**(i/365)) # amount of hashpwr bought
    
    data = np.delete(data,np.s_[-hashpwr_dur:],0)
    
    return(data)

def calculationsOpt(opt_reinvest,init_invest,init_hashpwr_price,invest_dur,hashpwr_dur,BTC_price,BTC_return,eff_red,hashpwr_price_red):
    """ Outputs the return on investment from the data output """
    data = calculations(opt_reinvest,init_invest,init_hashpwr_price,invest_dur,hashpwr_dur,BTC_price,BTC_return,eff_red,hashpwr_price_red)
    return(-data[-1,5])

' ################################# '
' Optimization '
' ################################# '

res_1 = minimize(calculationsOpt, np.zeros(invest_dur), method='L-BFGS-B', tol=0.01, bounds=[(0,1)]*invest_dur, args=(init_invest,init_hashpwr_price,invest_dur,hashpwr_dur,BTC_price,BTC_return,eff_red,hashpwr_price_red))
data = calculations(res_1.x,init_invest,init_hashpwr_price,invest_dur,hashpwr_dur,BTC_price,BTC_return,eff_red,hashpwr_price_red)

' ################################# '
' Plots '
' ################################# '

#plt.subplot(2, 2, 1)
fig1 = plt.figure()
plt.plot(data[:,0],data[:,3], '-')
plt.title('Reinvest rate []')
plt.ylabel('Reinvest rate []')
plt.xlabel('Day [#]')

#plt.subplot(2, 2, 2)
fig2 = plt.figure()
plt.plot(data[:,0], data[:,1], '-')
plt.title('Available hashpower [GH/s]')
plt.ylabel('Available hashpower [GH/s]')
plt.xlabel('Day [#]')

#plt.subplot(2, 2, 3)
fig3 = plt.figure()
plt.plot(data[:,0],data[:,4], '-')
plt.title('Value taken out per day [USD]')
plt.ylabel('Value taken out per day [USD]')
plt.xlabel('Day [#]')

#plt.subplot(2, 2, 4)
fig4 = plt.figure()
plt.plot(data[:,0],data[:,5], '-')
plt.title('Value taken out accumulated [USD]')
plt.ylabel('Value taken out accumulated [USD]')
plt.xlabel('Day [#]')

' ################################# '
' Prints '
' ################################# '

print('Optimization function evaluations: %d' % res_1.nfev)
print('Total return (USD): %d' % data[-1,5])
print('Remaining hashpower after the period optimized for (GH/s): %d' % data[-1,1])




