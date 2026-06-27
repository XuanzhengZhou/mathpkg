---
role: proof
locale: en
of_concept: "let-and-be-as-in-83-if-is"
source_book: gtm025
source_chapter: "Riemann-Stieltjes Integral"
source_section: "8.7"
---

Let $\varepsilon > 0$ be given. Since $[a, b]$ is compact (6.44), the function $f$ is uniformly continuous on $[a, b]$ (7.18). Thus there exists a $\delta > 0$ such that $|f(x) - f(y)| < \frac{\varepsilon}{\alpha(b) - \alpha(a) + 1}$ whenever $x, y \in [a

nonvoid set], we have

$$L(f_1, \alpha, \Delta_1) + L(f_2, \alpha, \Delta_2) \leq L(f_1, \alpha, \Delta) + L(f_2, \alpha, \Delta)$$
$$\leq L(f_1 + f_2, \alpha, \Delta)$$
$$\leq U(f_1 + f_2, \alpha, \Delta)$$
$$\leq U(f_1, \alpha, \Delta) + U(f_2, \alpha, \Delta)$$
$$\leq U(f_1, \alpha, \Delta_1) + U(f_2, \alpha, \Delta_2)$$
$$< L(f_1, \alpha, \Delta_1) + L(f_2, \alpha, \Delta_2) + \varepsilon.$$

It follows that $U(f_1 + f_2, \alpha, \Delta) - L(f_1 + f_2, \alpha, \Delta) < \varepsilon$ and hence $f_1 + f_2$ is integrable.

Next let $S_\alpha(f_j; [a, b]) = \gamma_j$ and let $\Gamma_j$ be such that

$$|L(f_j, \alpha, \Gamma_j) - \gamma_j| < \frac{\varepsilon}{6},$$

and

$$|U(f_j, \alpha, \Gamma_j) - \gamma_j| < \frac{\varepsilon}{6}.$$

It follows that $0 \leq U(f_j, \alpha, \Gamma_j) - L(f_j, \alpha, \Gamma_j) < \frac{\varepsilon}{3}$ for $j = 1, 2$. Setting $\Gamma = \Gamma_1 \cup \Gamma_2$, we have

$$L(f_1, \alpha, \Gamma_1) + L(f_2, \alpha, \Gamma_2) \leq L(f_1, \alpha, \Gamma) + L(f_2, \alpha, \Gamma)$$
$$\leq L(f_1 + f_2, \alpha, \Gamma)$$
$$\leq U(f_1 + f_2, \alpha, \Gamma)$$
$$\leq U(f_1
