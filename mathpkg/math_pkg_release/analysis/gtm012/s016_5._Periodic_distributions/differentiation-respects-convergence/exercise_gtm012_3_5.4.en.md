---
role: exercise
locale: en
chapter: "3"
section: "5"
exercise_number: 4
---

# Exercise 4

Compute $DF$ when $F$ is the distribution in part (c) or (d) of Exercise 1.

Recall from Exercise 1:
- (c) $F(u) = \int_0^{2\pi} u(x)\,dx$
- (d) $F(u) = \int_0^\pi u(x)(1+x)^7\,dx$

For a distribution defined by a function $v$, the derivative is $DF(u) = (DF_v)(u) = -F_v(Du) = -\frac{1}{2\pi}\int_0^{2\pi} v(x) Du(x)\,dx$. Use integration by parts to express the result as a distribution.
