---
role: proof
locale: en
of_concept: compact-sets-in-hausdorff-tvs
source_book: gtm003
source_chapter: "II"
source_section: "5"
---

**(i)** $A \cup B$ is compact: The finite union of compact sets in any topological space is compact.

**(ii)** $A + B$ is compact: The addition map $+: L \times L \to L$ is continuous. The product $A \times B$ is compact (Tychonoff's theorem for finite products). The continuous image of a compact set is compact, hence $A + B = +(A \times B)$ is compact.

**(iii)** $\lambda A$ is compact: The scalar multiplication map $x \mapsto \lambda x$ is continuous. The continuous image of the compact set $A$ is compact.

**(iv)** Circled hull of $A$ is compact when $K$ is locally compact: Let $S = \{\lambda \in K : |\lambda| \leq 1\}$ be the closed unit ball in $K$. Since $K$ is locally compact, $S$ is compact. The circled hull $\Gamma(A)$ is the image of $S \times A$ under the continuous scalar multiplication map $(\lambda, x) \mapsto \lambda x$. Since $S \times A$ is compact (Tychonoff), $\Gamma(A)$ is compact as the continuous image of a compact set.
