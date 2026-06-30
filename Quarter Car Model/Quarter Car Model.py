import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

#initiliazing variables
ms = 250
mu = 40
cs = 1000
kt = 150000
ks = 15000
t_span = (0, 10)
y0 = [5, 2, 3, 2]

#road position func
def r(t):
    return 0.05 * np.sin(2 * np.pi * t)

#returns values of dx1dt,dx2dt,dx3dt,dx4dt
def quarter_car(t, state):
    x1 = state[0] #body pos
    x2 = state[1] #body vel
    x3 = state[2] #wheel pos
    x4 = state[3] #wheel vel
    dx1dt = x2 
    dx2dt =((1/ms)*(ks*(x3 - x1) - cs*(x4 - x2)))
    dx3dt = x4
    dx4dt = ((-ks*(x3 - x1) - cs*(x4 - x2) + kt*(r(t) - x3))*(1/mu))

    return [dx1dt,dx2dt,dx3dt,dx4dt]

t_eval = np.linspace(0, 10, 500)

# Solve
solution = solve_ivp(quarter_car, t_span, y0, t_eval=t_eval)

#Plot

plt.plot(solution.t, solution.y[0], label='Body(sprung)')
plt.plot(solution.t, solution.y[2], label='Wheel(unsprung)')
plt.xlabel("Time/(s)")
plt.ylabel("Position")
plt.show()