---
role: proof
locale: en
of_concept: positive-function-zero-integral-on-set
source_book: gtm018
source_chapter: "V"
source_section: "25"
---
**Proof.** Write $F_0 = \{x : f(x) > 0\}$ and $F_n = \{x : f(x) \geq 1/n\}$, $n=1,2,\dots$. Since $E-F_0$ has measure zero, it suffices to show $\mu(E \cap F_0) = 0$. But
$$0 = \int_{E \cap F_n} f d\mu \geq \frac{1}{n} \mu(E \cap F_n) \geq 0,$$
so $\mu(E \cap F_n) = 0$ for all $n$. Since $F_0 = \bigcup_{n=1}^{\infty} F_n$, $\mu(E \cap F_0) \leq \sum_n \mu(E \cap F_n) = 0$.
