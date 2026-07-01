# Spring-Damper System in a Quarter Car Model :

It expands from a single mass to a 2-DOF model moving along a single vertical axis, the forces that govern this particular system have been split into a suspensions force and a tire force.

This diagram depicts a spring-damper system within a quarter car:

<img width="520" height="454" alt="2-Figure2-1" src="https://github.com/user-attachments/assets/05fadfb6-512e-4f4d-894d-b6b54cea8d37" />


Note:

	Sprung Mass - Car body,Engine,Passengers,Cargo
	Unsprung Mass - Wheel,Tyre,Brake assembly,Parts of the suspension system

Likewise,The quarter car model can also be denoted by the second-order ODE:

	my’’ + cy’ + ky = F(t)

There are 4 state variables in this model:

  	x1 = x_s (sprung-mass displacement)
  	x2 = x_s’ (sprung-mass velocity)
  	x3 = x_us (unsprung-mass displacement)
  	x4 = x_us’ (unsprung-mass velocity)

In this model it is converted into four first order ODEs:

  	x’1 = x2
  	x’2 = [1/m]*[-ks(x1-x3)-cs(x2-x4)]
  	x’3 = x4
  	x’4 = [1/m]*[ks(x1-x3)+cs(x2-x4)-k1(x3-r)]

This is a image includes a position of road position against time as well as a graph plot of the velocity and position on both a sprung and unsprung graph against time using the following values:

	ms(spring mass) = 250
	mu(unsprung mass) = 80
	cs(damping coeffecient spring) = 1000
	kt(tyre spring constant) = 75000
	ks(sprung section spring constant) = 15000
	time = 10
	intial sprung positon= 5
	intial sprung velocity= 2
	intial unsprung positon= 3
	intial unsprung velocity= 2

<img width="1131" height="692" alt="Screen Shot 2026-07-01 at 5 50 27 PM" src="https://github.com/user-attachments/assets/2825cf86-914c-4366-be7c-9a2933a0335e" />
