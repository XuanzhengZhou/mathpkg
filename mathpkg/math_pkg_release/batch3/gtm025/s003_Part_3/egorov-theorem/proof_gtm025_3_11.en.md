---
role: proof
locale: en
of_concept: egorov-theorem
source_book: gtm025
source_chapter: "3"
source_section: "11"
---

**Proof.** For $m \in \mathbb{N}$, let
$$E_m = \{x \in X : |f(x) - f_n(x)| < 1/m \text{ for all } n \geq m\}.$$
These are measurable, $E_1 \subset E_2 \subset \cdots$, and $\bigcup E_m$ contains the convergence set. Since $\mu(E_m') \to 0$, select $m_k$ with $\mu(E_{m_k}') < \delta/2^k$ and set $A = \bigcap E_{m_k}$. Then $\mu(A') < \delta$ and $f_n \to f$ uniformly on $A$. $\square$
