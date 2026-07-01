import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Initialization for values
m = 10
c = 75
k = 1000
y0 = [1, 0]
t_span = (0, 2)

# ODE system that returns values of dx1dt and dx2dt
def system(t, state):
    x1 = state[0]
    x2 = state[1]

    dx1dt = x2
    dx2dt = (-c*x2 + -k*x1)/m 

    return [dx1dt, dx2dt]

# Time evaluation points
t_eval = np.linspace(0, 2, 500)

# Solve
solution = solve_ivp(system, t_span, y0, t_eval=t_eval)

#Plot
plt.plot(solution.t, solution.y[0])
plt.plot(solution.t, solution.y[1])

plt.xlabel("Time")
plt.ylabel("Position/Velocity")
plt.title("Velocity and Position against Time")
plt.grid(True)

plt.show()
