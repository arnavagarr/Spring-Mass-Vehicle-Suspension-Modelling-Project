# Single Mass Spring-Damper System:

In this 1-DOF Model,it includes a simplified model of a single mass moving along a single axis, the forces that govern motion include a spring(k) and a damper(c)

This diagram depicts a single mass spring-damper system:

<img width="391" height="520" alt="image" src="https://github.com/user-attachments/assets/52d7c13e-c0ef-4f0b-86d6-3b95d4c9f985" />

The model can be denoted by the second-order ODE:

	my’’ + cy’ + ky = F(t)

We define two state space variables representing displacement(x1) and velocity(x2)

This equation must be converted into two first order ODEs:

	x’1 = x2

	x’2 = x’’1 = (1/m)*(F(t)-cx2-kx1)


This is a graph plot of the velocity and position against time using the following values:

	m(mass) = 10
	c(damping coefficient) = 75
	k(spring constant) = 1000
	initial position = 1
	initial velocity = 0(at rest)
	time span = 2

<img width="894" height="652" alt="Screen Shot 2026-07-01 at 5 29 48 PM" src="https://github.com/user-attachments/assets/0b8a58b7-1320-4942-897d-3a1707448e78" />

Another graph with the same system using different values this time:

	m(mass) = 100
	c(damping coefficient) = 250
	k(spring constant) = 10000
	initial position = 1
	initial velocity = 0(at rest)
	time span = 7.5
	
<img width="936" height="594" alt="Screen Shot 2026-07-01 at 5 33 30 PM" src="https://github.com/user-attachments/assets/e521bb64-57ff-451e-a4e8-de020e67a20f" />
