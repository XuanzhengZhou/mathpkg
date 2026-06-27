---
role: proof
locale: en
of_concept: preimage-borel-measurable
source_book: gtm025
source_chapter: "3"
source_section: "11"
---

**Proof.** Let $\mathcal{S} = \{S \subset \mathbb{R} : f^{-1}(S) \in \mathcal{A}\}$. Then $\mathcal{S}$ contains $\emptyset$, is closed under countable unions (since $f^{-1}(\bigcup S_n) = \bigcup f^{-1}(S_n)$), and closed under complementation (adjusting for $\pm\infty$). Thus $\mathcal{S}$ is a $\sigma$-algebra.

Since $f$ is measurable, $f^{-1}(]a, \infty]) \in \mathcal{A}$ for all $a$, and similarly $f^{-1}([-\infty, b[) \in \mathcal{A}$. For any open interval $]a, b[$,
$$f^{-1}(]a, b[) = f^{-1}([-\infty, b[) \cap f^{-1}(]a, \infty]) \in \mathcal{A}.$$
Every open set is a countable union of open intervals, so $\mathcal{S}$ contains all open sets, hence all Borel sets. $\square$
