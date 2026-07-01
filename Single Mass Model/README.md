# Single Mass Spring-Damper System:

In this 1-DOF Model,it includes a simplified model of a single mass moving along a single axis, the forces that govern motion include a spring(k) and a damper(c)

This diagram depicts a single mass spring-damper system:


<img width="253" height="243" alt="images" src="https://github.com/user-attachments/assets/7804803f-1495-4d15-bf0b-a63ae59b0c47" />

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

<img width="586" height="449" alt="image" src="https://github.com/user-attachments/assets/579ee851-6927-48f4-9cf0-ba73759fc0c4" />

Another graph with the same system using different values this time:

	m(mass) = 100
	c(damping coefficient) = 250
	k(spring constant) = 10000
	initial position = 1
	initial velocity = 0(at rest)
	time span = 7.5
	
<img width="572" height="449" alt="Screen Shot 2026-07-01 at 12 04 15 PM" src="https://github.com/user-attachments/assets/9ac788b1-af92-495d-a0d2-ada697c57880" />

