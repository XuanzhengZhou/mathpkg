---
role: exercise
locale: en
chapter: "Chapter 16"
section: "16.7"
exercise_number: 1
---
# Exercise 1

Let $u \in L^2(\mathbb{C}^n)$ and let $\chi \in C_0^\infty(\mathbb{C}^n)$ be a smooth mollifier with $\chi \geq 0$, $\int \chi = 1$, and $\operatorname{supp} \chi \subset B(0,1)$. For $\varepsilon > 0$, define $\chi_\varepsilon(z) = \varepsilon^{-2n} \chi(z/\varepsilon)$ and the convolution

$$u_\varepsilon(z) = \int_{\mathbb{C}^n} u(\zeta) \chi_\varepsilon(z - \zeta) dV(\zeta).$$

Prove that $u_\varepsilon \in C^\infty(\mathbb{C}^n)$.

*Hint:* Differentiate under the integral sign. For any multi-index $\alpha$, $\partial^\alpha u_\varepsilon(z) = \int u(\zeta) \partial_z^\alpha \chi_\varepsilon(z - \zeta) dV(\zeta)$. Since $\chi_\varepsilon \in C_0^\infty$, all derivatives are continuous and the integral converges absolutely.
