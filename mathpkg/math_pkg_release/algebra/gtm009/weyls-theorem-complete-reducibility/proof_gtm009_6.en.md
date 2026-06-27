---
role: proof
locale: en
of_concept: weyls-theorem-complete-reducibility
source_book: gtm009
source_chapter: "6"
source_section: "6.1-6.3"
---

\textbf{Proof sketch.} The key steps are:

1. Reduce to showing that for any $L$-submodule $W$ of $V$ of codimension 1, there exists a complementary 1-dimensional $L$-submodule (using induction).

2. Construct the Casimir operator $c_\phi$: If $\phi: L \rightarrow \mathfrak{gl}(V)$ is a faithful representation with nondegenerate trace form $\beta(x,y) = \text{Tr}(\phi(x)\phi(y))$, let $\{x_i\}$ be a basis of $L$ and $\{y_i\}$ the dual basis relative to $\beta$. Define $c_\phi = \sum \phi(x_i)\phi(y_i) \in \text{End } V$. Then $c_\phi$ commutes with $\phi(L)$ and $\text{Tr}(c_\phi) = \dim L \neq 0$.

3. For the general case, decompose $L$ into simple ideals and construct Casimir operators for each.

4. If $W \subset V$ is an $L$-submodule of codimension 1, consider the action on $V/W$. The Casimir operator acts as a scalar on $V/W$ (by Schur's Lemma). Its eigenspace decomposition yields the complementary submodule.

The complete proof requires detailed analysis of the Casimir operator and its properties.
