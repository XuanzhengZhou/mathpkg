---
role: exercise
locale: en
chapter: "7"
section: "7. Convolution of distributions"
exercise_number: 2
---

# Exercise 2

Prove the identities (7) and (11):

(7) $\delta * u = u$, $(D^k \delta) * u = D^k u$, for $u \in \mathcal{P}$.

(11) $\delta * F = F * \delta = F$, for $F \in \mathcal{P}'$.

For (7), use the definition $(F * u)(x) = F(T_x \tilde{u})$ with $F = \delta$ and $F = D^k \delta$, noting that $\delta(T_x \tilde{u}) = \tilde{u}(-x) = u(x)$ and $(D^k \delta)(T_x \tilde{u}) = (-1)^k D^k(T_x \tilde{u})(0)$.

For (11), use the definition $(F * G)(u) = F(G^\sim * u)$ with $G = \delta$, noting that $\delta^\sim * u = \delta * u = u$ by (7).
