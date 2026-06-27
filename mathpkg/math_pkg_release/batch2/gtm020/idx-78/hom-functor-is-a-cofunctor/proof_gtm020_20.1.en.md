---
role: proof
locale: en
of_concept: hom-functor-is-a-cofunctor
source_book: gtm020
source_chapter: "20"
source_section: "1"
---

We verify the two cofunctor axioms.

1. For the identity morphism $1_X: X \to X$, we have $[1_X, K]u = u \circ 1_X = u$ for every $u \in [X, K]$. Hence $[1_X, K] = 1_{[X, K]}$.

2. For composable morphisms $g: Z \to Y$ and $f: Y \to X$, and for any $u \in [X, K]$, we compute:
   $$[fg, K]u = u(fg) = (uf)g = [g, K](uf) = [g, K]([f, K]u) = ([g, K] \circ [f, K])(u).$$
   Thus $[fg, K] = [g, K] \circ [f, K]$.

Since both axioms hold, $[-, K]$ is a cofunctor from $\mathbf{A}$ to $\mathbf{ens}$.
