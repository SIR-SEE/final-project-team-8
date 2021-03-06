# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 09:02:08 2020

@author: forss
"""
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def deriv(y, t, N, beta, k, delta):
    S, E, I, R = y
    dSdt = -beta * S * I / N
    dEdt = (beta * S * I / N - k * E) * epsilon
    dIdt = delta * E - k * I
    dRdt = k * I
    return dSdt, dEdt, dIdt, dRdt

#Parameters
epsilon = 0.5                       # A number that simulates the effects of safety measures, lockdowns, restrictions etc.
m = 0.021                           # Mortality rate
N = 2000                            # Population
beta = 2.5                          # Number of people infected per infected and per time unit
k=1/7                               # Amount of people recovered per time unit
S0, E0, I0, R0 = N-1, 1, 0, 0       # initial conditions: one infected, rest susceptible
t = np.linspace(0, 99, 100)         # Grid of time points (in days)
y0 = S0, E0, I0, R0                 # Initial conditions vector
delta = 1/5

                                    # Integrate the SIR equations over the time grid, t.
ret = odeint(deriv, y0, t, args=(N, beta, k, delta))
S, E, I, R = ret.T

D = R * m                           # Dead people = Recovered people * mortality rate
R = R - D                           # Number of recovered gets subtracted by the number of dead

def plotsir(t, S, E, I, R, D):      
  f, ax = plt.subplots(1,1,figsize=(10,4))
  ax.plot(t, S, 'b', alpha=0.7, linewidth=2, label='Susceptible')
  ax.plot(t, E, 'y', alpha=0.7, linewidth=2, label='Exposed')
  ax.plot(t, I, 'r', alpha=0.7, linewidth=2, label='Infected')
  ax.plot(t, R, 'g', alpha=0.7, linewidth=2, label='Recovered')
  ax.plot(t, D, 'k', alpha=0.7, linewidth=2, label='Deceased')

  ax.set_xlabel('Time (days)')

  ax.yaxis.set_tick_params(length=0)
  ax.xaxis.set_tick_params(length=0)
  ax.grid(b=True, which='major', c='w', lw=2, ls='-')
  legend = ax.legend()
  legend.get_frame().set_alpha(0.5)
  
  for spine in ('top', 'right', 'bottom', 'left'):
      ax.spines[spine].set_visible(False)
  plt.savefig("Plot.png")
  plt.show();
  
  
                                  # Plot the graph
plotsir(t, S, E, I, R, D)
