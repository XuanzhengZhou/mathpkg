---
role: proof
locale: en
of_concept: birkhoff-isomorphism-theorem
source_book: gtm026
source_chapter: "3"
source_section: "3.3"
---

The passage from $\xi$ to $X\lambda \cdot \xi$ is injective because $X\lambda$ is an epimorphism in $\mathcal{K}$, so that $V$ is injective on objects. The diagram below shows that $f: (X, \xi') \longrightarrow (Y, \theta')$ is a $\mathbf{T}'$-homomorphism if and only if $f: (X, \xi')V \longrightarrow (X, \theta')V$ is a $\mathbf{T}$-homomorphism (since $X\lambda$ is epi). Therefore, $V$ is a full subcategory.

Let $(X, \xi) \in \mathcal{A}$. There exists a unique $\mathbf{T}$-homomorphism $\xi^{\#}: (XT, X\mu) \longrightarrow (X, \xi)$ such that $\xi^{\#} \cdot U^T = \xi$. Since $X\lambda: (XT, X\mu) \longrightarrow XT'$ is the reflection into $\mathcal{A}$, there exists a unique $\mathbf{T}$-homomorphism $\bar{\xi}: XT' \longrightarrow (X, \xi)$ in $\mathcal{A}$ with $\bar{\xi} \cdot X\lambda = \xi^{\#}$. Then $(X, \xi) = (XT', \xi_X) \cdot \bar{\xi}$, showing that every object of $\mathcal{A}$ is in the image of $V$. Thus $V$ is essentially surjective, establishing the isomorphism $\mathcal{K}^{T'} \cong \mathcal{A}$.

The algebraicity of $(\mathcal{A}, U)$ in $\text{Struct}(\mathcal{K})$ follows from the fact that $(\mathcal{K}^{T'}, U^{T'})$ is algebraic and $V$ is an isomorphism over $\mathcal{K}$.
