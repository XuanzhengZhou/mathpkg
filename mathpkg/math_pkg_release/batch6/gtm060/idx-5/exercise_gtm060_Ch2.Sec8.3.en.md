---
role: exercise
locale: en
chapter: "2"
section: "8"
exercise_number: 3
---

**PROBLEM.** During his walk in outer space, the cosmonaut A. Leonov threw the lens cap of his movie camera towards the earth. Describe the motion of the lens cap with respect to the spaceship, taking the velocity of the throw as 10 m/sec.

**ANSWER.** The lens cap will move relative to the cosmonaut approximately in an ellipse with major axis about 32 km and minor axis about 16 km. The center of the ellipse will be situated 16 km in front of the cosmonaut in his orbit, and the period of circulation around the ellipse will be equal to the period of motion around the orbit.

**Hint.** Take as unit of length the radius of the space ship's circular orbit, and choose a unit of time so that the period of revolution around this orbit is $2\pi$. Study solutions to Newton's equation
$$\ddot{\mathbf{r}} = -\frac{\mathbf{r}}{r^3},$$
close to the circular solution with $r_0 = 1$, $\varphi_0 = t$. Seek solutions in the form
$$\mathbf{r} = \mathbf{r}_0 + \mathbf{r}_1, \quad \varphi = \varphi_0 + \varphi_1, \quad r_1 \ll 1, \; \varphi_1 \ll 1.$$

By the theorem on the differentiability of a solution with respect to its initial conditions, the functions $r_1(t)$ and $\varphi_1(t)$ satisfy a system of linear differential equations (equations of variation) up to small amounts which are of higher than first order in the initial deviation.

Substituting the expressions for $r$ and $\varphi$ in Newton's equation yields the variational equations:
$$\ddot{r}_1 = 3r_1 + 2\dot{\varphi}_1, \quad \ddot{\varphi}_1 = -2\dot{r}_1.$$

Solving for the initial conditions $(r_1(0) = \varphi_1(0) = \dot{\varphi}_1(0) = 0, \dot{r}_1(0) = -1/800)$ gives the answer above. Disregarding small quantities of second order gives an effect of under $1/800$ of the one obtained (on the order of 10 meters on one loop). Thus the lens cap describes a 30 km ellipse in an hour-and-a-half, returns to the space ship on the side opposite the earth, and goes past at a distance of a few tens of meters.
