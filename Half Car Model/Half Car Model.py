import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


# initialzing

ms = 600       # sprung mass
muf = 40       # front unsprung mass
mur = 40       # rear unsprung mass

ksf = 15000    # front spring stiffness
ksr = 15000    # rear spring stiffness

csf = 1000     # front damping coef
csr = 1000     # rear damping coef

ktf = 150000   # front tyre stiffness
ktr = 150000   # rear tyre stiffness

a = 1.2        # CG to front axle
b = 1.3        # CG to rear axle


Iyy = 1200     # pitch moment of inertia


t_span = (0,10)

# Initial conditions

y0 = [
    0.05, 0,    # body position, velocity
    0, 0,       # pitch angle, angular velocity
    0, 0,       # front wheel position, velocity
    0, 0        # rear wheel position, velocity
]


def r(t):
    if 2 < t < 2.2:
        return 0.05*np.sin(np.pi*(t-2)/0.2)
    else:
        return 0
    
def half_car(t,state):
  
    x1 = state[0] # body position
    x2 = state[1] # body velocity

    x3 = state[2] # pitch angle
    x4 = state[3] # pitch angular velocity

    x5 = state[4] # front wheel position
    x6 = state[5] # front wheel velocity

    x7 = state[6] # rear wheel position
    x8 = state[7] # rear wheel velocity



    front_body = x1 + a*x3
    rear_body = x1 - b*x3



    front_body_velocity = x2 + a*x4
    rear_body_velocity = x2 - b*x4


    frontForce = (ksf*(front_body - x5) + csf*(front_body_velocity - x6))
    rearForce = (ksr*(rear_body - x7)  + csr*(rear_body_velocity - x8))


    # Body vertical motion
    dx1dt = x2
    dx2dt = -(frontForce + rearForce)/ms


    # Body pitch motion
    dx3dt = x4
    dx4dt = (frontForce*a - rearForce*b)/Iyy


    # Front wheel
    dx5dt = x6
    dx6dt = (frontForce - ktf*(x5-r(t)))/muf

    # Rear wheel
    dx7dt = x8
    dx8dt = (rearForce - ktr*(x7-r(t)))/mur


    return [dx1dt,dx2dt,dx3dt,dx4dt,dx5dt,dx6dt,dx7dt,dx8dt]

# solve

t_eval = np.linspace(0,10,500)

solution = solve_ivp(half_car,t_span,y0,t_eval=t_eval)


#plotting

fig, axis = plt.subplots(2,2, figsize=(12,8))


# Body motion

axis[0,0].plot(solution.t, solution.y[0], label="Body")
axis[0,0].set_title("Body Vertical Position")
axis[0,0].set_xlabel("Time (s)")
axis[0,0].set_ylabel("Position (m)")
axis[0,0].legend()
axis[0,0].grid(True)


# Pitch

axis[0,1].plot(solution.t, solution.y[2], label="Pitch")

axis[0,1].set_title("Body Pitch Angle")
axis[0,1].set_xlabel("Time (s)")
axis[0,1].set_ylabel("Angle (rad)")
axis[0,1].legend()
axis[0,1].grid(True)



# Wheels

axis[1,0].plot(solution.t, solution.y[4], label="Front Wheel")
axis[1,0].plot(solution.t, solution.y[6], label="Rear Wheel")

axis[1,0].set_title("Wheel Positions")
axis[1,0].set_xlabel("Time (s)")
axis[1,0].set_ylabel("Position (m)")
axis[1,0].legend()
axis[1,0].grid(True)



# Road

axis[1,1].plot(solution.t,r(solution.t),label="Road")

axis[1,1].set_title("Road Input")
axis[1,1].set_xlabel("Time (s)")
axis[1,1].set_ylabel("Road Height (m)")
axis[1,1].legend()
axis[1,1].grid(True)


plt.tight_layout()
plt.show()
