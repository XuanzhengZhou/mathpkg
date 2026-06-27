---
role: proof
locale: en
of_concept: timelike-vectors-bundle-components
source_book: gtm048
source_chapter: "1"
source_section: "1.1"
---

Let $\mathcal{A}$ be a connected component of $\mathcal{T}$. Since $\psi$ is a diffeomorphism of $\mathcal{T}$ onto itself, $\psi(\mathcal{A})$ is also a component of $\mathcal{T}$. We claim $\mathcal{T} = \mathcal{A} \cup \psi(\mathcal{A})$.

Define $\mathcal{B} = \mathcal{A} \cup \psi(\mathcal{A})$ and $\mathcal{C} = \mathcal{T} \setminus \mathcal{B}$. Since $\mathcal{B}$ is a union of components, it is both open and closed in $\mathcal{T}$, and so $\mathcal{C}$ is also open and closed in $\mathcal{T}$. Let $\Pi: \mathcal{T} \to M$ be the bundle projection.

We claim $\Pi(\mathcal{B}) \cap \Pi(\mathcal{C}) = \varnothing$. Suppose not; then there exist $(x, Z) \in \mathcal{B}$ and $(x, Y) \in \mathcal{C}$ for some $x \in M$. Let $\mathcal{Y} \subset M_x \cap \mathcal{T}$ be the component of the fiber containing $(x, Y)$ (by Exercise 1.1.9(a), each fiber $M_x \cap \mathcal{T}$ has exactly two components). Since $\mathcal{C}$ is a union of components of $\mathcal{T}$, we have $\mathcal{Y} \subset \mathcal{C}$.

Now either $(x, Z)$ or $(x, -Z)$ lies in $\mathcal{Y}$, while both belong to $\mathcal{B}$ by definition of $\mathcal{B}$. Thus $\mathcal{B} \cap \mathcal{Y} \neq \varnothing$, and since $\mathcal{B}$ is a union of components, $\mathcal{Y} \subset \mathcal{B}$. This gives $\mathcal{B} \cap \mathcal{C} \neq \varnothing$, a contradiction.

Therefore $\Pi(\mathcal{B}) \cap \Pi(\mathcal{C}) = \varnothing$ and $\Pi(\mathcal{B}) \cup \Pi(\mathcal{C}) = M$. Since $M$ is connected, $\Pi(\mathcal{C}) = \varnothing$, so $\mathcal{C} = \varnothing$. Hence $\mathcal{T} = \mathcal{A} \cup \psi(\mathcal{A})$.

If $\mathcal{A} \cap \psi(\mathcal{A}) = \varnothing$, then $\mathcal{T}$ has exactly two components. Otherwise $\mathcal{A} = \psi(\mathcal{A})$ and $\mathcal{T}$ is connected.
