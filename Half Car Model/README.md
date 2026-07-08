

# Spring-Damper System in a Half Car Model:

This model expands the quarter car into a 4-DOF system by considering both the front and rear suspension of the vehicle, as well as the vehicle body's pitching motion. It provides a more realistic representation of vehicle dynamics by accounting for vertical motion and rotational motion simultaneously.

This diagram depicts a spring-damper system within a half car:

<img width="509" height="754" alt="image" src="https://github.com/user-attachments/assets/8671a13e-0d81-4e35-92a9-297b276d0593" />

### Note:

* **Sprung Mass** – Vehicle body, engine, passengers, cargo
* **Unsprung Front Mass** – Front wheel, tyre, brake assembly, front suspension components
* **Unsprung Rear Mass** – Rear wheel, tyre, brake assembly, rear suspension components

There are **8 state variables** in this model:

```
x1 = z_s   (sprung mass displacement)
x2 = z_s'  (sprung mass velocity)

x3 = θ      (body pitch angle)
x4 = θ'     (body pitch rate)

x5 = z_uf   (front unsprung mass displacement)
x6 = z_uf'  (front unsprung mass velocity)

x7 = z_ur   (rear unsprung mass displacement)
x8 = z_ur'  (rear unsprung mass velocity)
```

The second-order equations of motion are converted into **eight first-order ODEs**:

```
x'1 = x2

x'2 = (1/ms)[
    -kf(z_s + l_fθ - z_uf)
    -cf(z_s' + l_fθ' - z_uf')
    -kr(z_s - l_rθ - z_ur)
    -cr(z_s' - l_rθ' - z_ur')
]

x'3 = x4

x'4 = (1/Iyy)[
    -l_f(kf(z_s + l_fθ - z_uf) + cf(z_s' + l_fθ' - z_uf'))
    +l_r(kr(z_s - l_rθ - z_ur) + cr(z_s' - l_rθ' - z_ur'))
]

x'5 = x6

x'6 = (1/muf)[
     kf(z_s + l_fθ - z_uf)
    +cf(z_s' + l_fθ' - z_uf')
    -ktf(z_uf - r_f)
]

x'7 = x8

x'8 = (1/mur)[
     kr(z_s - l_rθ - z_ur)
    +cr(z_s' - l_rθ' - z_ur')
    -ktr(z_ur - r_r)
]
```

This image includes a graph of the front and rear road profiles against time, along with plots of the sprung mass displacement, pitch angle, and the front and rear unsprung mass responses using the following values:

```
ms (sprung mass) = 600
muf (front unsprung mass) = 60
mur (rear unsprung mass) = 60

kf (front suspension spring constant) = 18000
kr (rear suspension spring constant) = 18000

cf (front damping coefficient) = 1500
cr (rear damping coefficient) = 1500

ktf (front tyre stiffness) = 180000
ktr (rear tyre stiffness) = 180000

lf (CG to front axle distance) = 1.2
lr (CG to rear axle distance) = 1.6

Iyy (pitch moment of inertia) = 1200

simulation time = 10 s

initial sprung position = 0
initial sprung velocity = 0

initial pitch angle = 0
initial pitch rate = 0

initial front unsprung position = 0
initial front unsprung velocity = 0

initial rear unsprung position = 0
initial rear unsprung velocity = 0
```

*Insert simulation results image here.*

---

This matches the tone and formatting of your previous READMEs while extending naturally to the half-car model. If your implementation uses different notation (e.g., `a`/`b` instead of `lf`/`lr`, or different parameter values), you can substitute those directly.
