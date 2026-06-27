---
role: proof
locale: en
of_concept: chain-rule-analytic
source_book: gtm011
source_chapter: "III"
source_section: "2"
---

Fix $z_0$ in $G$ and choose a positive number $r$ such that $B(z_0; r) \subset G$. We must show that if $0 < |h_n| < r$ and $\lim h_n = 0$ then $\lim \{h_n^{-1}[g(f(z_0 + h_n)) - g(f(z_0))]\}$ exists and equals $g'(f(z_0)) f'(z_0)$.

Let $w_0 = f(z_0)$ and $k_n = f(z_0 + h_n) - f(z_0)$. Since $f$ is continuous, $k_n \to 0$. If $f'(z_0) \neq 0$ or $k_n \neq 0$ for large $n$, the usual computation works:
$$\frac{g(f(z_0 + h_n)) - g(f(z_0))}{h_n} = \frac{g(w_0 + k_n) - g(w_0)}{k_n} \cdot \frac{f(z_0 + h_n) - f(z_0)}{h_n} \to g'(w_0) f'(z_0).$$

The case where infinitely many $k_n = 0$ is handled by noting that then $g'(w_0) = 0$ must hold for the limit to exist.
