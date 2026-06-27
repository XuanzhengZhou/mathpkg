---
role: exercise
locale: en
chapter: "6"
section: "§6. Fourier series"
exercise_number: 3
---

# Exercise 3

Suppose $u \in \mathcal{C}$ and suppose $b_n, c_n$ are the real Fourier coefficients of $u$ as defined in (10). Show that

$$u_N(x) = \frac{1}{2\pi} \int_0^{2\pi} D_N(x - y)u(y) \, dy,$$

where

$$D_N(x) = \frac{\sin(N + \frac{1}{2})x}{\sin\frac{1}{2}x}.$$

The function $D_N$ is called the Dirichlet kernel. Thus

$$u_N = D_N * u.$$
