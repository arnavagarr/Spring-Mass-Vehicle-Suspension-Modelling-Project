import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

#initiliazing variables
ms = 250
mu = 80
cs = 500
kt = 75000
ks = 15000
t_span = (0, 10)
y0 = [5, 2, 3, 2]

#road position func
def r(t):
    return 0.05 * np.sin(2 * np.pi * t)

#returns values of dx1dt,dx2dt,dx3dt,dx4dt
def quarter_car(t, state):

    x1 = state[0] #sprung pos
    x2 = state[1] #sprung vel
    x3 = state[2] #unsprung pos
    x4 = state[3] #unsprung vel
    
    dx1dt = x2 
    dx2dt =(-ks*(x1 - x3) - cs*(x2 - x4)) / ms
    dx3dt = x4
    dx4dt = ( ks*(x1 - x3) + cs*(x2 - x4) - kt*(x3 - r(t)) ) / mu

    return [dx1dt,dx2dt,dx3dt,dx4dt]

t_eval = np.linspace(0, 10, 500)

# Solve
solution = solve_ivp(quarter_car, t_span, y0, t_eval=t_eval)
road = r(solution.t)

#plot section

figure , axis = plt.subplots(1, 3)
#sprung section
axis[0].plot(solution.t, solution.y[0], label='Position' ,color ='red')
axis[0].plot(solution.t, solution.y[1], label='Velocity' ,color ='blue')
axis[0].legend()
#unsprung section
axis[1].plot(solution.t, solution.y[2], label='Position' ,color ='red')
axis[1].plot(solution.t, solution.y[3], label='Velocity' ,color ='blue')
axis[1].legend()
axis[2].plot(solution.t, road, label='Road Position' ,color ='green')
axis[2].legend()

axis[0].set_xlabel("Time")
axis[0].set_ylabel("Sprung Values")

axis[1].set_xlabel("Time")
axis[1].set_ylabel("Unsprung Values")

axis[2].set_xlabel("Time")
axis[2].set_ylabel("Road Position")




plt.show()
