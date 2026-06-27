---
role: proof
locale: en
of_concept: projective-plane-implies-complete-mols
source_book: gtm006
source_chapter: "5"
source_section: "5. Latin Squares"
---

**Proof.** Let $\mathcal{P}$ be a finite projective plane of order $n$. Then $\mathcal{P}$ may be coordinatized by a planar ternary ring $(R, T)$ of order $n$, where $R = \{0, 1, \dots, n-1\}$ (by the coordinatization theorem of Chapter 5).

By Lemma 5.7, for each $x \in R$, $x \neq 0$, the $n \times n$ matrix $\{x\}$ defined by $T(x, i, j)$ in row $i$, column $j$ is a Latin square, and for $x \neq y$, $\{x\}$ is orthogonal to $\{y\}$. This yields $n-1$ mutually orthogonal Latin squares of order $n$, which by definition constitutes a complete set.
