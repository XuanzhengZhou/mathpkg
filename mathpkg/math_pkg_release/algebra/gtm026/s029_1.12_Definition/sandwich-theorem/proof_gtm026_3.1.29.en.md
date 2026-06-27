---
role: proof
locale: en
of_concept: sandwich-theorem
source_book: gtm026
source_chapter: "3"
source_section: "1.29"
---

(1) Since $V$ has a left adjoint, if $U$ has a left adjoint then $W$ has a left adjoint by the Composition Theorem for Adjoints (2.2.30). Conversely, suppose $W$ has a left adjoint $F': \mathcal{K} \to \mathcal{A}$. Let $\mathbf{T}$ be the algebraic theory induced by the adjunction $(F', W, \eta', \varepsilon')$. For each $K \in \mathcal{K}$, let $(K, \xi)$ be the corresponding $\mathbf{T}$-algebra.

Consider the pair of $\mathcal{A}$-morphisms:
\[
KF'UF' \xrightarrow{\xi F'} KF' \qquad KF'UF' \xrightarrow{KF'\varepsilon'} KF'
\]
Let $p = \mathrm{coeq}(a, b)$ in $\mathcal{A}$ (which exists since $\mathcal{A}$ has coequalizers). Then one verifies that $KF' \xrightarrow{p} A$ with $K\eta'.pW: (K, \xi) \to AU$ is a $\mathbf{T}$-homomorphism, and that this construction yields a left adjoint to $U$.

(2) If $W$ is algebraic, then by (1) $U$ has a left adjoint. The proof that $U$ creates coequalizers of $U$-absolute pairs uses the fact that $V$ creates such coequalizers (being algebraic) and $W$ creates such coequalizers (being algebraic), together with the commutativity of the diagram, to lift coequalizers through $U$.
