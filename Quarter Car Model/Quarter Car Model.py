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
y0 = [0.05, 0, 0, 0]

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
road = r(solution.t)


#plot section

figure , axis = plt.subplots(1, 3)
#postion -graph 0
axis[0].plot(solution.t, solution.y[0], label='Body' ,color ='red')
axis[0].plot(solution.t, solution.y[2], label='Wheel' ,color ='green')
axis[0].legend()

axis[0].set_xlabel("Time/(s)")
axis[0].set_ylabel("Position")

axis[0].set_title("Position against Time")
axis[0].grid(True)

#velocity -graph 1
axis[1].plot(solution.t, solution.y[1], label='Body' ,color ='blue')
axis[1].plot(solution.t, solution.y[3], label='Wheel' ,color ='orange')
axis[1].legend()

axis[1].set_xlabel("Time/(s)")
axis[1].set_ylabel("Velociity")

axis[1].set_title("Velocity against Time")
axis[1].grid(True)

#road postion -graph 2
axis[2].plot(solution.t, road, label='Road Position' ,color ='black')
axis[2].legend()

axis[2].set_xlabel("Time/(s)")
axis[2].set_ylabel("Road Position")

axis[2].set_title("Road Position against Time")
axis[2].grid(True)

plt.show()
