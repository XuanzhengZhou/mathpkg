---
role: proof
locale: en
of_concept: proper-smooth-mappings-nonempty-open
source_book: gtm014
source_chapter: "5"
source_section: "5. The Whitney Embedding Theorem"
---

By I,5.11 there exists a proper mapping of $X \to \mathbb{R}$. Compose this mapping with any linear injection of $\mathbb{R} \to \mathbb{R}^m$ to obtain a proper mapping of $X \to \mathbb{R}^m$. To show that the set of proper mappings is open, let $f: X \to \mathbb{R}^m$ be proper and let $V_x = \{y \in \mathbb{R}^m \mid d(y, f(x)) < 1\}$. Let $V = \bigcup_{x \in X} V_x$ in $J^0(X, \mathbb{R}^m) = X \times \mathbb{R}^m$. The continuity of $f$ guarantees that $V$ is open and clearly $f$ is in $M(V)$. Now let $g$ be in $M(V)$; then $g$ is proper, for $g^{-1}(\overline{B}_r(y)) \subset f^{-1}(B_{r+1}(y))$. Since $f$ is proper, $g^{-1}(\overline{B}_r(y))$ is a closed subset of a compact set and thus compact.
