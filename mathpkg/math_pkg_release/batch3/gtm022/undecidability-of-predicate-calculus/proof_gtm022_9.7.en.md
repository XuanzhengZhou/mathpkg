---
role: proof
locale: en
of_concept: undecidability-of-predicate-calculus
source_book: gtm022
source_chapter: "IX"
source_section: "7"
---

The proof reduces the undecidability of $\operatorname{Pred}(V, \{\rho\})$ (with a 4-ary $\rho$, which follows from the undecidability of $\mathcal{N}$) to that of $\operatorname{Pred}(V, \{r\})$ with binary $r$. The key lemma encodes a 4-ary relation on $S$ as a binary relation on $S' = \{K\} \cup S^2 \cup S^4$ via a carefully constructed $r$. A translation $f: P(V, \{\rho\}) \to P(V, \{r\})$ is defined such that $f(p)$ is a theorem iff $p$ is a theorem, preserving theoremhood while reducing the arity.
