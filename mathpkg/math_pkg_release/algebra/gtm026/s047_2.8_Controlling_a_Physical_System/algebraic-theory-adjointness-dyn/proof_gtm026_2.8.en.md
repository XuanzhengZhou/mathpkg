---
role: proof
locale: en
of_concept: algebraic-theory-adjointness-dyn
source_book: gtm026
source_chapter: "2"
source_section: "2.8"
---

By the Beck theorem of 3.1.9, to prove that $\text{Dyn}(X)$ is algebraic over $\mathcal{K}$ we need only establish that $U$ creates coequalizers of $U$-contractible pairs; here, the details are so similar to the proof of 3.1.9 "1 implies 2" that we will omit them. By the proof of 3.1.9 "3 implies 1," the semantics comparison functor is an isomorphism. The diagram

$$
\begin{array}{c c c c c} Q \eta X & Q X^@ X & Q \mu_0 & Q X^@ \\ \delta^@ X & Q X & \delta & Q \\ \delta & Q & \delta & Q \end{array}
$$

proves that $Q \rho.\delta^@ = \delta$ so that the inverse to $\Phi$ is as advertised (functoriality is clear from the discussion below). To show that $X^@$ is the free algebraic theory over $X$ we must first observe that $\rho$ is natural; but $\eta X$ is natural and $\mu_0$ is natural since $fX^@$ is a dynamorphism by definition (see 2.2.18 "(i) implies (ii)"). Now consider 2.10 with $T$ and $\lambda$ arbitrary. Define $V: \mathcal{K}^T \longrightarrow \text{Dyn}(X)$ by $(Q, \xi)V = (Q, Q \lambda.\xi)$. $V$ is a well-defined homomorphism in $\text{Struct}(\mathcal{K})$ because $\lambda$ is natural. Let $\lambda^{\#}: X^@ \longrightarrow T$ be the theory map corresponding to $V.\Phi: \mathcal{K}^T \longrightarrow \mathcal{K}^{X^@}$ as in 3.2.9; then we have

$$
A \lambda^{\#} = AX^@ \xrightarrow{A \eta_T X^@} ATX^@ \xrightarrow{(AT \lambda.A \mu_T)^@} AT
$$

The diagram proves that $\rho.\lambda^{\#} = \lambda$. If also $\rho.\psi = \lambda$, the corresponding homomorphism $V' : \mathcal{K}^{\mathbf{T}} \longrightarrow \mathcal{K}^{\mathbf{X}}$ is such that $V.\Phi^{-1}$ is the passage

$$(Q, \xi) \longmapsto (Q, QX \xrightarrow{Q\rho} QX^@ \xrightarrow{Q\psi} QT \xrightarrow{\xi} Q)$$

which proves, since $Q\rho.Q\psi = Q\lambda$, that $V = V'$ and hence $\lambda^{\#} = \psi$.
