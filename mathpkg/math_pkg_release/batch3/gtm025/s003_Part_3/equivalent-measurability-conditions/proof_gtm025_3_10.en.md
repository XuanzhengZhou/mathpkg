---
role: proof
locale: en
of_concept: equivalent-measurability-conditions
source_book: gtm025
source_chapter: "3"
source_section: "10"
---

**Proof.** The implications are proved as follows:
(iii) $\Rightarrow$ (ii): $U$ and $A \cap U$ measurable $\Rightarrow$ $U \cap A'$ measurable, so $\iota(U) = \iota(U \cap A) + \iota(U \cap A')$.
(ii) $\Rightarrow$ (i): For arbitrary $T$ with $\iota(T) < \infty$, choose open $U \supset T$ with $\iota(U) < \iota(T) + \varepsilon$. Then
$$\iota(T) + \varepsilon > \iota(U) = \iota(U \cap A) + \iota(U \cap A') \geq \iota(T \cap A) + \iota(T \cap A').$$
(i) $\Rightarrow$ (iv): If $A$ is measurable, $U$ open, then $A \cap U$ is measurable (10.10), hence a countable union of measurable sets (trivially).
(iv) $\Rightarrow$ (iii): If $U \cap A = \bigcup F_n$ with $F_n$ measurable, then $U \cap A$ is measurable since $\mathcal{M}_\iota$ is a $\sigma$-algebra. $\square$
