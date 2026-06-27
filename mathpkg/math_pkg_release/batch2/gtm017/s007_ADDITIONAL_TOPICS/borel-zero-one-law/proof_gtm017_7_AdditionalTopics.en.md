---
role: proof
locale: en
of_concept: borel-zero-one-law
source_book: gtm017
source_chapter: "7"
source_section: "Additional Topics"
---

Assume the $A_i$ are independent. By De Morgan's laws,
$$A_i \text{ f.o.} = \overline{A_i \text{ i.o.}} = \bigcup_{n=1}^{\infty} \bigcap_{i=n}^{\infty} \bar{A}_i,$$
and $P(\bigcap_{i=n}^{\infty} \bar{A}_i) = \prod_{i=n}^{\infty} (1 - P(A_i)) \leq \exp(-\sum_{i=n}^{\infty} P(A_i))$ (using $1-x \leq e^{-x}$).

If $\sum P(A_i)$ diverges, then for each $n$, $\sum_{i=n}^\infty P(A_i) = \infty$, so $P(\bigcap_{i=n}^\infty \bar{A}_i) = 0$. Hence $P(A_i \text{ f.o.}) = 0$ and $P(A_i \text{ i.o.}) = 1$.

If $\sum P(A_i) < \infty$, the first Borel-Cantelli lemma gives $P(A_i \text{ i.o.}) = 0$. Thus $P(A_i \text{ i.o.})$ can only be $0$ or $1$.
