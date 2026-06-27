---
role: proof
locale: en
of_concept: birkhoff-variety-theorem-set
source_book: gtm026
source_chapter: "3"
source_section: "3.4"
---

**1 implies 2.** $\mathcal{A}$ has and $V$ preserves small limits. If $f : (X, \xi) \longrightarrow (Y, \theta)$ is a $\mathbf{T}$-homomorphism with $(Y, \theta)$ in $\mathcal{A}$, then the $\mathbf{T}$-subalgebra $Xf$ of $(Y, \theta)$ (see 1.4.32) is again in $\mathcal{A}$, and there is a commutative diagram factoring $f$ through its image.

Since the cardinality of $Xf$ is at most the cardinality of $X$, it follows from the General Adjoint Functor Theorem (2.2.24) that every $\mathbf{T}$-algebra has a reflection in $\mathcal{A}$. Moreover, all such reflections are surjective. To prove surjectivity, let $\Gamma : X \longrightarrow A$ denote the reflection of the $\mathbf{T}$-algebra $X$ in $\mathcal{A}$. Let $(p, i)$ be the image factorization of $\Gamma$. Since $X\Gamma$ is in $\mathcal{A}$, there exists a unique $\bar{p} : A \longrightarrow X\Gamma$ with $\Gamma.\bar{p} = p$. Then $\Gamma.\bar{p}.i = p.i = \Gamma$, so $\bar{p}.i = \mathrm{id}_A$, which implies $i$ is surjective. Therefore $\Gamma$ is surjective. It is clear that $V$ is closed under $U^{\mathbf{T}}$-split epimorphisms since, with $\mathcal{K} = \mathbf{Set}$, this is equivalent to the condition "$\mathcal{A}$ is closed under quotients."

**2 implies 1.** Define $\mathcal{B}$ to be the full subcategory of all $\mathbf{T}$-algebras which are a quotient of a subalgebra of an element of $\mathcal{A}$. Clearly, $\mathcal{B}$ is closed under quotients, or equivalently, $\mathcal{B}$ is closed under $U^{\mathbf{T}}$-split epimorphisms. Now let $\Gamma : (XT, X\mu) \longrightarrow A$ be a reflection of $(XT, X\mu)$ in $\mathcal{A}$ with $\Gamma$ surjective. Let $Q \in \mathcal{B}$, so there exist $A_1$ in $\mathcal{A}$, a subalgebra $S$ of $A_1$ with inclusion $i : S \longrightarrow A_1$, and a surjective $\mathbf{T}$-homomorphism $q : S \longrightarrow Q$. Let $f : (XT, X\mu) \longrightarrow Q$ be an arbitrary $\mathbf{T}$-homomorphism. Using the reflection property and the surjectivity of $q$, one lifts $f$ to a map into $A_1$, which shows that $Q$ lies in $\mathcal{A}$. Thus $\mathcal{B} \subseteq \mathcal{A}$. Since $\mathcal{A} \subseteq \mathcal{B}$ by construction, $\mathcal{A} = \mathcal{B}$, and $\mathcal{A}$ is closed under products, subalgebras, and quotients as required.
