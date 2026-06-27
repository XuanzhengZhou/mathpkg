---
role: proof
locale: en
of_concept: kernel-intersection-equals-kernel-of-gcd
source_book: gtm023
source_chapter: "XIII"
source_section: "§1. Polynomials in a linear transformation"
---

Since $d \mid f$ and $d \mid g$, it follows from (13.1) that

$$K(d) \subset K(f) \quad \text{and} \quad K(d) \subset K(g),$$

whence

$$K(d) \subset K(f) \cap K(g). \tag{13.2}$$

On the other hand, since $d$ is the greatest common divisor of $f$ and $g$, there exist polynomials $f_1, g_1 \in \Gamma[t]$ such that

$$d = f_1 f + g_1 g.$$

Thus if $x \in K(f) \cap K(g)$, we have $f(\varphi)x = 0$ and $g(\varphi)x = 0$, and so

$$d(\varphi)x = f_1(\varphi)f(\varphi)x + g_1(\varphi)g(\varphi)x = 0.$$

Hence $x \in K(d)$, which yields

$$K(d) \supset K(f) \cap K(g). \tag{13.3}$$

Together, (13.2) and (13.3) establish $K(d) = K(f) \cap K(g)$.
