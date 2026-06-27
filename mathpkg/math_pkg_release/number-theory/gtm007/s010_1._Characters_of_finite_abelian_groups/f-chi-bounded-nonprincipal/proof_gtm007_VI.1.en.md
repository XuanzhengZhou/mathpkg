---
role: proof
locale: en
of_concept: f-chi-bounded-nonprincipal
source_book: gtm007
source_chapter: "VI"
source_section: "§1. Characters of finite abelian groups"
---

From the Euler product, for $R(s) > 1$,
$$
\log L(s,\chi) = \sum_{p} \sum_{n=1}^\infty \frac{\chi(p)^n}{n p^{ns}} = f_\chi(s) + F_\chi(s),
$$
where $F_\chi(s) = \sum_{p} \sum_{n \geq 2} \frac{\chi(p)^n}{n p^{ns}}$ is absolutely convergent for $R(s) > 1/2$, hence bounded near $s = 1$. Since $L(1,\chi) \neq 0$ (Theorem 1) and $L(s,\chi)$ is continuous, $\log L(s,\chi)$ converges to a finite value as $s \to 1^+$. Therefore $f_\chi(s) = \log L(s,\chi) - F_\chi(s)$ remains bounded.
