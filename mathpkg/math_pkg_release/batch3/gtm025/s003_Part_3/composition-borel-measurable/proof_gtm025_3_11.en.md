---
role: proof
locale: en
of_concept: composition-borel-measurable
source_book: gtm025
source_chapter: "3"
source_section: "11"
---

**Proof.** For $a \in \mathbb{R}$,
$$(\varphi \circ f)^{-1}(]a, \infty]) = f^{-1}(\varphi^{-1}(]a, \infty]))$$
$$= f^{-1}\big((\varphi^{-1}(]a, \infty]) \cap \mathbb{R}) \cup \{\infty : \varphi(\infty) > a\} \cup \{-\infty : \varphi(-\infty) > a\}\big).$$
By hypothesis, $\varphi^{-1}(]a, \infty]) \cap \mathbb{R}$ is a Borel set in $\mathbb{R}$, so its preimage under $f$ is in $\mathcal{A}$ by (11.4). The sets involving $\pm\infty$ are either $\emptyset$ or the whole space. $\square$
