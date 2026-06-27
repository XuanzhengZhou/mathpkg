---
role: exercise
locale: en
chapter: "IV"
section: "Problems"
exercise_number: 5
---

Define

$$\Delta_n = \det \begin{pmatrix}
x_1 & 1 & & & 0 \\
-1 & x_2 & 1 & & \\
& -1 & x_3 & \ddots & \\
& & \ddots & \ddots & 1 \\
0 & & & -1 & x_n
\end{pmatrix}$$

Show that $\Delta_n = x_n \Delta_{n-1} + \Delta_{n-2}$ for $n > 2$, with the initial values

$$\Delta_1 = x_1; \qquad \Delta_2 = x_1 x_2 + 1.$$
