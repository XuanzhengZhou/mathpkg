---
role: proof
locale: en
of_concept: theorem-15
source_book: gtm026
source_chapter: "1"
source_section: "3.6"
---

1 implies 2. $\mathcal{A}$ has and $V$ preserves small limits. If $f: (X, \xi) \longrightarrow (Y, \theta)$ is a $\mathbf{T}$-homomorphism with $(Y, \theta)$ in $\mathcal{A}$ then the $\mathbf{T}$-subalgebra $Xf$ of $(Y, \theta)$ (1.4.32) is again in $\mathcal{A}$ and there is a commutative diagram

As the cardinal of $Xf$ is at most as large as the cardinal of $X$, it follows from the general adjoint functor theorem of 2.2.24 that every T-algebra has a reflection in $\mathcal{A}$. Moreover, all such reflections are surjective. To prove it, let $\Gamma: X \longrightarrow A$ denote the reflection of the T-algebra $X$ in $\mathcal{A}$. Let $(p, i)$ be the image factorization of $\Gamma$. Since $X\Gamma$ is in $\mathcal{A}$ there exists unique $\bar{p}: A \longrightarrow X\Gamma$ with $\Gamma.\bar{p} = p$. As $\Gamma.\bar{p}.i = p.i = \Gamma$, $\bar{p}.i = \text{id}_A$ and $i$ is surjective. Therefore, $\Gamma$ is surjective. It is clear that $V$ is closed under $U^{\mathbf{T}}$-split epimorphisms since, with $\mathcal{K} = \mathbf{Set}$, this is the same as “$\mathcal{A}$ is closed under quotients.”

2 implies 1. Define $\mathcal{B}$ to be the full subcategory of all T-algebras which are a quotient of a subalgebra of an element of $\mathcal{A}$. Clearly, $\mathcal{B}$ is closed under quotients or, equivalently, $\mathcal{B}$ is closed under $U^{\mathbf{T}}$-split epimorphisms. Now let $\Gamma:(XT, X\mu) \longrightarrow A$ be a reflection of $(XT, X\mu)$ in $\mathcal{A}$ with $\Gamma$ surjective. Let $Q \in \mathcal{B}$ so that there exists $A_1$ in $\mathcal{A}$, a subalgebra $S$ of $A_1$ with inclusion $i: S \longrightarrow A_1$ and a surjective T-homomorphism $q: S \longrightarrow Q$. Let $f:(XT, X\mu) \longrightarrow Q$ be an arbitrary T-homomorphism. Using the
