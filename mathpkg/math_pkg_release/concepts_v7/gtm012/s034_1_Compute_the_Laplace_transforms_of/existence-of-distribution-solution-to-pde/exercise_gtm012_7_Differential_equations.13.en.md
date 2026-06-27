---
role: exercise
locale: en
chapter: "7"
section: "Differential equations"
exercise_number: 13
---

# Exercise 13

Again let

$$\tilde{u}(t) = u(-t), \qquad T_s u(t) = u(t-s).$$

If $F \in \mathcal{L}'$ and $u \in \mathcal{L}$, set

$$\tilde{F} * u(t) = F(T_{-t} u).$$

(a) Suppose $F = F_v$, where $v: \mathbb{R} \to \mathbb{C}$ is continuous, $v(t) = 0$ for $t \leq -M$, and $e^{-at} v(t)$ is bounded. Show that for each $u \in \mathcal{L}$ the convolution integral

$$\tilde{v} * u(t) = \int \tilde{v}(t-s) u(s) \, ds$$

exists and equals $\tilde{F} * u(t)$.

(b) Show that for each $F \in \mathcal{L}'$ and $u \in \mathcal{L}$, the function $\tilde{F} * u$ is in $\mathcal{L}$.
