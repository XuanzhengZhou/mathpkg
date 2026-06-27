---
role: exercise
locale: en
chapter: "11"
section: "11.3"
exercise_number: 3
---
# Exercise 11.3

Fix $F \in A$. Show that $Z_F$ is upper semicontinuous on $\Omega$; i.e., for each $\lambda_0 \in \Omega$,

$$Z_F(\lambda_0) \geq \limsup_{\lambda \to \lambda_0} Z_F(\lambda),$$

where $Z_F(\lambda) = \max_{x \in f^{-1}(\lambda)} |F(x)|$.

*(Note: A real-valued function $u$ defined on $\Omega$ is subharmonic on $\Omega$ if (i) $u$ is upper semicontinuous at each $\lambda \in \Omega$, and (ii) for each closed disk $\Delta = \{|\lambda - \lambda_0| \leq r\} \subset \Omega$, $u(\lambda_0) \leq \frac{1}{2\pi} \int_0^{2\pi} u(\lambda_0 + re^{i\theta}) d\theta$.)*
