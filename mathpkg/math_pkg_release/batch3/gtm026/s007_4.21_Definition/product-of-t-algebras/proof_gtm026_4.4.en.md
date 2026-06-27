---
role: proof
locale: en
of_concept: product-of-t-algebras
source_book: gtm026
source_chapter: "4"
source_section: "4"
---

**Proof of (4.27).** Let $(X_i, \xi_i)$ be a family of $T$-algebras and $X = \prod X_i$. Define $\xi: XT \longrightarrow X$ componentwise: for $\bar{x} \in XT$, the $i$-th component of $\bar{x}\xi$ is defined by the requirement that $\mathrm{pr}_i: (X, \xi) \longrightarrow (X_i, \xi_i)$ be a $T$-homomorphism. That is:

$$\bar{x}\xi = (\langle \bar{x}, \mathrm{pr}_i T \cdot \xi_i \rangle)_{i \in I}$$

To verify the $T$-algebra axioms, consider the diagram with projections. Everything commutes by the definition of $\xi$ except possibly the associativity condition. But applying the principle that two functions into $X$ are equal if and only if they are equal followed by each projection, the required commutativity follows from the $T$-algebra axioms for each $(X_i, \xi_i)$. The unit law is proved by the same reasoning. This completes the proof that $(X, \xi)$ is a $T$-algebra, and by construction it is the unique structure making all projections $T$-homomorphisms. $\square$
