---
role: exercise
locale: en
chapter: "5"
section: "5. The wave equation"
exercise_number: 2
---

# Exercise 2

In the problem

$$\frac{\partial^2 u}{\partial t^2} = \frac{\partial^2 u}{\partial x^2}, \quad x \in (0, \pi), \quad t > 0,$$
$$u(0, t) = u(\pi, t) = 0,$$
$$u(x, 0) = g(x), \quad \frac{\partial u}{\partial t}(x, 0) = h(x),$$

with $c = 1$, suppose $g$, $h$, and $u$ are smooth functions. Show, by computing the derivative with respect to $t$, that

$$\int_0^\pi \left| \frac{\partial}{\partial x} u(x, t) \right|^2 dx + \int_0^\pi \left| \frac{\partial}{\partial t} u(x, t) \right|^2 dx$$

is constant. (This expresses conservation of energy: the first term represents potential energy, from the tension, while the second term represents kinetic energy.)
