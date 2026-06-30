# Spring-Damper System in a Quarter Car Model :

It expands from a single mass to a 2-DOF model moving along a single vertical axis, the forces that govern this particular system have been split into a suspensions force and a tire force.

This diagram depicts a spring-damper system within a quarter car:

<img width="520" height="454" alt="2-Figure2-1" src="https://github.com/user-attachments/assets/05fadfb6-512e-4f4d-894d-b6b54cea8d37" />

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
    

