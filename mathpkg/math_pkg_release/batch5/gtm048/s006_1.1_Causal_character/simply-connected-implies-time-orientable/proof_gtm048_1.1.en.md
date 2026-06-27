---
role: proof
locale: en
of_concept: simply-connected-implies-time-orientable
source_book: gtm048
source_chapter: "1"
source_section: "1.1"
---

A detailed proof is deferred to Section 8.2.3. The essential idea sketched here is as follows.

Let $\mathcal{T} \subset TM$ be the set of all timelike tangent vectors. Define a map $\psi: \mathcal{T} \to \mathcal{T}$ by $\psi(x, X) = (x, -X)$. Let $\mathcal{A}$ be a connected component of $\mathcal{T}$, and set $\mathcal{B} = \mathcal{A} \cup \psi(\mathcal{A})$. One must show $\mathcal{T} = \mathcal{B}$. If $\mathcal{C} = \mathcal{T} \setminus \mathcal{B} \neq \varnothing$, then both $\mathcal{B}$ and $\mathcal{C}$ are open and closed in $\mathcal{T}$.

Let $\Pi: TM \to M$ be the bundle projection. A key claim is that $\Pi(\mathcal{B}) \cap \Pi(\mathcal{C}) = \varnothing$: otherwise there would exist $(x, Z) \in \mathcal{B}$ and $(x, Y) \in \mathcal{C}$ in the same fiber, and using that $\mathcal{B}$ and $\mathcal{C}$ are unions of connected components, one derives a contradiction from the fact that each fiber $M_x \cap \mathcal{T}$ has exactly two components (Exercise 1.1.9(a)) and both must lie entirely in one of $\mathcal{B}$, $\mathcal{C}$.

Thus $\Pi(\mathcal{B})$ and $\Pi(\mathcal{C})$ form a disconnection of $M$ via open sets. Since $M$ is connected, $\Pi(\mathcal{C}) = \varnothing$, so $\mathcal{C} = \varnothing$ and $\mathcal{T} = \mathcal{B} = \mathcal{A} \cup \psi(\mathcal{A})$. If $\mathcal{A} \cap \psi(\mathcal{A}) = \varnothing$, then $\mathcal{T}$ has two components and $(M, g)$ is time orientable. The simply connected hypothesis is used to rule out the case $\mathcal{A} = \psi(\mathcal{A})$.

(Complete proof: see Section 8.2.3 of GTM048.)
