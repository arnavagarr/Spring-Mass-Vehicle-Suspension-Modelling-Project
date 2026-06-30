# Quarter Car:

It expands from a single mass to a 2-DOF model moving along a single vertical axis, the forces that govern this particular system have been split into a suspensions force and a tire force.

There are 4 state variables in this model:

  x1 = x_s (sprung-mass displacement)
  x2 = x_s’ (sprung-mass velocity)
  x3 = x_us (unsprung-mass displacement)
  x4 = x_us’ (unsprung-mass velocity)

In this model it is converted into four first order ODEs:

  x’1 = x2
  x’2  = [1/m]*[-ks(x1-x3)-cs(x2-x4)]
  x’3 = x4
  x’4  = [1/m]*[ks(x1-x3)+cs(x2-x4)-k1(x3-r)]
