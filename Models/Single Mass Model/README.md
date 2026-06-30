In this 1-DOF Model,it includes a simplified model of a single mass moving along a single axis, the forces that govern motion include a spring(k) and a damper(c)

The model is covered by the second-order ODE:

		my’’ + cy’ + ky = F(t)

We define two state space variables representing displacement(x1) and velocity(x2)

This equation must be converted into two first order ODEs:

		x’1 = x2

		x’2 = x’’1 = (1/m)*(F(t)-cx2-kx1)

This is an image of a single mass spring-damper system:
<img width="253" height="243" alt="images" src="https://github.com/user-attachments/assets/7804803f-1495-4d15-bf0b-a63ae59b0c47" />
