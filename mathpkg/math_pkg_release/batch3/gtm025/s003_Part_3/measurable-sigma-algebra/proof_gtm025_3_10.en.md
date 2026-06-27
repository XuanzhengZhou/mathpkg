---
role: proof
locale: en
of_concept: measurable-sigma-algebra
source_book: gtm025
source_chapter: "3"
source_section: "10"
---

**Proof.** Let $B_n = A_n \setminus \bigcup_{k=1}^{n-1} A_k$ (with $B_1 = A_1$). The $B_n$ are pairwise disjoint and measurable (by 10.10), and $\bigcup B_n = \bigcup A_n$.

For any $T \subset X$, by (10.9.i) and countable subadditivity:
$$\mu(T) = \sum_{n=1}^{\infty} \mu(T \cap B_n) + \mu\left(T \cap \bigcap_{n=1}^{\infty} B_n'\right) \geq \mu\left(T \cap \bigcup B_n\right) + \mu\left(T \cap \left(\bigcup B_n\right)'\right).$$

Subadditivity gives the reverse inequality, so equality holds and $\bigcup B_n = \bigcup A_n$ is measurable. With (10.8), $\mathcal{M}_\mu$ is a $\sigma$-algebra.

Setting $T = \bigcup B_k$ in (10.9.i): $\mu(\bigcup B_n) = \sum \mu(B_n) + \mu(\emptyset) = \sum \mu(B_n)$, so $\mu$ is countably additive. $\square$
