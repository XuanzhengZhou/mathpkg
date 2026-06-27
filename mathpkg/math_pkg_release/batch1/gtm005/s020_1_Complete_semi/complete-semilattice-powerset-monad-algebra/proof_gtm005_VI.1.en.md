---
role: proof
locale: en
of_concept: complete-semilattice-powerset-monad-algebra
source_book: gtm005
source_chapter: "VI"
source_section: "1"
---

An algebra for the powerset monad $\mathcal{P}: \mathbf{Set} \to \mathbf{Set}$ (unit $\eta_X(x) = \{x\}$, multiplication $\mu_X(\mathcal{A}) = \bigcup \mathcal{A}$) is a set $X$ with $h: \mathcal{P}(X) \to X$ satisfying $h(\{x\}) = x$ and $h(\bigcup \mathcal{A}) = h(\{h(A) : A \in \mathcal{A}\})$.

Define $x \leq y$ iff $h(\{x, y\}) = y$. This gives a complete join-semilattice with $\bigvee S = h(S)$. The algebra axioms translate to: $\bigvee\{x\} = x$ (unit law), and for $\mathcal{A} \subseteq \mathcal{P}(X)$, $\bigvee(\bigcup \mathcal{A}) = \bigvee\{\bigvee A : A \in \mathcal{A}\}$ (complete associativity, from the multiplication law).

Conversely, any complete join-semilattice $(X, \bigvee)$ yields an algebra via $h(S) = \bigvee S$, and the axioms correspond to the defining properties of $\bigvee$.
