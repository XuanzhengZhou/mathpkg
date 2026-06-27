---
locale: en
of_concept: mapping-space-of-principal-g-bundle-is-path-connected
role: proof
source_book: gtm020
source_chapter: "3"
source_section: "3.3"
---

The fact that the space is nonempty is equivalent to the assertion that $P$ is isomorphic to $f^*(E_G)$ for some map $f$: $B \rightarrow B_G$, see 3(12.3), which in turn is part of a bundle morphism $u$: $P \rightarrow E_G$ inducing $f$. Thus, $u \in \text{Map}_G(P, E_G)$ and the space is nonempty.

To see that it is path connected, we consider two elements $u$, $u' \in \text{Map}_G(P, E_G)$ inducing maps $f$, $f'$: $B \rightarrow B_G$ where $P$ is isomorphic to both $f^*(E_G)$ and $f'^*(E_G)$. Hence, $f$ and $f'$ are homotopic with a morphism of bundles $(w, h)$: $P \times [0, 1] \rightarrow E_G$ such that $w(x, 0) = u(x)$ and $w(x, 1) = u'(x)$, see 3(12.4). Thus, $w$ defines a path from $u$ to $u'$ in $\text{Map}_G(P, E_G)$, and proves the last statement.
