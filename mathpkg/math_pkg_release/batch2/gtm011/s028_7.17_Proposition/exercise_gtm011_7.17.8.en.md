---
role: exercise
locale: en
chapter: "7"
section: "17"
exercise_number: 8
---

Let $u > 0$ and $v > 0$ and express $\Gamma(u) \Gamma(v)$ as a double integral over the first quadrant of the plane. By changing to polar coordinates show that

$$\Gamma(u) \Gamma(v) = 2\Gamma(u+v) \int_{0}^{\pi/2} (\cos \theta)^{2u-1} (\sin \theta)^{2v-1} \, d\theta.$$

The function

$$B(u, v) = \frac{\Gamma(u) \Gamma(v)}{\Gamma(u+v)}$$

is called the beta function. By changes of variables show that

$$B(u, v) = \int_{0}^{1} t^{u-1} (1-t)^{v-1} \, dt = \int_{0}^{\infty} \frac{t^{u-1}}{(1+t)^{u+v}} \, dt.$$

Can this be generalized to the case when $u$ and $v$ are complex numbers with positive real part?
