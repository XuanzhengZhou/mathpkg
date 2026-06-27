---
role: proof
locale: en
of_concept: dual-of-continuous-linear-maps-space
source_book: gtm003
source_chapter: "IV"
source_section: "4"
---

**Proof.** If $v = \sum x_i \otimes y_i'$, the mapping $v \mapsto f$ defined by $f(u) = \sum \langle u x_i, y_i' \rangle$ for $u \in \mathcal{L}(E, F)$ is obviously a linear map of $E \otimes F'$ into $\mathcal{L}_s(E, F)'$. It is also biunivocal, since the bilinear form $(v, u) \mapsto f(u)$ places even the subspace $E' \otimes F$ of $\mathcal{L}(E, F)$ (Chapter III, Section 7) in separated duality with $E \otimes F'$ (Section 1, Example 4).

There remains to show that this mapping is onto $\mathcal{L}_s(E, F)'$. Since $\mathcal{L}_s(E, F)$ is a subspace of the product space $F^E$, every $g \in \mathcal{L}_s(E, F)'$ is the restriction of a continuous linear form on $F^E$. Hence, by Theorem 4.3, $g$ is of the form

$$u \mapsto g(u) = \sum \langle u x_i, y_i' \rangle$$

for suitable finite subsets $\{x_i\} \subset E$ and $\{y_i'\} \subset F'$, which completes the proof. $\square$
