import numpy as np
from scipy.integrate import odeint
from scipy.integrate import solve_ivp
import matlabplot.py as plt


#Initialization section for the variables:
m = 10
c = 5
k = 2
y0 = [1,0]
t_span = (0,10)



#Function that returns dx/dt
def system(t, state):

    x1 = state[0] #position
    x2 = state[1] #velocity

    dx1dt = x2
    dx2dt = (-1/m) * (c*x2 + k*x1)

    return [dx1dt,dx2dt]

#Solve ODE
t_eval = np.linspace(0,10,500)

solution = solve_ivp(system, t_span, y0, t_eval=t_eval)
#Plot the results
import matplotlib.pyplot as plt

plt.plot(solution.y[0], solution.y[1])

plt.xlabel("Position")
plt.ylabel("Velocity")
plt.title("Phase Space: Velocity vs Position")
plt.grid(True)

plt.show()