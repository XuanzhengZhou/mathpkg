---
role: exercise
locale: en
chapter: "21"
section: "SS 21"
exercise_number: "21.60"
---

Define $f$ on $R$ by $f(x) = \exp(-x^2/2)$. Use (21.59.a) to prove that $\hat{f} = f$.

Hints. Write $\hat{f} = \varphi$. By (21.59.a), $\varphi'(y) = i(2\pi)^{-\frac{1}{2}} \int_R (-x) \exp(-x^2/2) \exp(-iyx) dx$.
Integrate by parts to obtain $\varphi'(y) = -y\varphi(y)$ for all $y \in R$.
Conclude that $\frac{d}{dy}[\varphi(y) \exp(y^2/2)] = 0$ for all $y \in R$.
Show $\varphi(0) = 1$ by using polar coordinates:
$$2\pi\varphi(0)^2 = \int_R \exp(-x^2/2)dx \int_R \exp(-y^2/2)dy = \int_0^{2\pi}\int_0^\infty \exp(-r^2/2)r dr d\theta = 2\pi.$$
