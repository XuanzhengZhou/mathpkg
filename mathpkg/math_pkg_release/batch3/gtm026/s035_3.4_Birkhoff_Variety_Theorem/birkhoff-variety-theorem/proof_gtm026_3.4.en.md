---
role: proof
locale: en
of_concept: birkhoff-variety-theorem
source_book: gtm026
source_chapter: "3"
source_section: "3.4"
---

First, observe that $X\lambda : (XT, X\mu) \longrightarrow (XT', \xi_X)$ is a $\mathbf{T}$-homomorphism.

To prove that $V$ is closed under reflections: Let $(Y, \theta')$ be a $\mathbf{T}'$-algebra and let $f : (XT, X\mu) \longrightarrow (Y, \theta')V$ be a $\mathbf{T}$-homomorphism. Define $\bar{f} = (X\eta.f)T'.\theta' : (XT', X\mu') \longrightarrow (Y, \theta')$. Then $\bar{f}$ is a $\mathbf{T}'$-homomorphism, and consequently $\bar{f} : (XT', \xi_X) \longrightarrow (Y, \theta')V$ is a $\mathbf{T}$-homomorphism. The universal property of the reflection yields $X\lambda.\bar{f} = f$, and $\bar{f}$ is unique with this property because $X\lambda$ is epi in $\mathcal{K}$. This proves that $(XT', \xi_X; X\lambda)$ is a reflection of $(XT, X\mu)$ in $V$.

To prove that $V$ is closed under $U^{\mathbf{T}}$-split epimorphisms: Let $(X, \xi')$ be a $\mathbf{T}'$-algebra, let $f : (X, X\lambda.\xi') \longrightarrow (Y, \theta)$ be a $\mathbf{T}$-homomorphism, and let $d : Y \longrightarrow X$ in $\mathcal{K}$ be such that $d.f = \mathrm{id}_Y$. It suffices to prove that there exists a $\mathbf{T}$-homomorphism $\theta' : (YT', \xi_Y) \longrightarrow (Y, \theta)$ such that the same diagrams as in the proof of 3.3 (applied to $\xi'$) prove that $(Y, \theta')$ is a $\mathbf{T}'$-algebra. The desired $\theta'$ is given by $dT'.\xi'.f$.

These two closure properties, together with the results of sections 3.2 and 3.3, establish the equivalence of the two characterizations in the theorem.
