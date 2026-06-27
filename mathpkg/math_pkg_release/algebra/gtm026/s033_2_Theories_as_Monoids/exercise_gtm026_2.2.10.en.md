---
role: exercise
locale: en
chapter: "2"
section: "2"
exercise_number: 10
---

([Appelgate '65], [Manes '67, 1.4.5]). Let $\mathbf{T}$ be an algebraic theory in $\mathcal{L}$, let $\mathbf{S}$ be an algebraic theory in $\mathcal{K}$, and let $H: \mathcal{K} \longrightarrow \mathcal{L}$ be a functor. A functor $\Gamma: \mathcal{K}^{\mathbf{S}} \longrightarrow \mathcal{L}^{\mathbf{T}}$ is said to be *over* $H$ if $\Gamma \cdot U^{\mathbf{T}} = U^{\mathbf{S}} \cdot H$, generalizing the case $H = \mathrm{id}$. A *theory map relative to* $H$ is a natural transformation $\lambda: H T \longrightarrow S H$ satisfying the coherence conditions with the theory structures.

**(a)** Show that the passage $(A, \xi: AS \longrightarrow A)\Gamma = (AH, A\lambda \cdot \xi H)$ establishes a bijection between functors $\Gamma$ over $H$ and theory maps $\lambda$ relative to $H$.

[*Hint:* if $(AS, A\mu_S)\Gamma = (ASH, \xi_A: ASHT \longrightarrow ASH)$, define $A\lambda = A\eta_S HT \cdot \xi_A$.]

**(b)** Let $H: \mathcal{K} \longrightarrow \mathcal{L}$ be the underlying set functor from topological spaces. Interpret the unique continuous (surjective) map induced by the identity function from discrete $X$ to the space $(X, \tau)$ between their $\beta$-compactifications as a theory map relative to $H$; show that the corresponding $\Gamma$ is the identity functor on compact Hausdorff spaces.

**(c)** Compute the theory map relative to $H$ in the context shown below:

[*Hint:* recall from 1.32 the theory for rings over monoids.]

**(d)** Let $\mathbf{T}$ be the algebraic theory in $\mathbf{Set}$ corresponding to lattices [i.e., $(\Omega, E)$-algebras for the variety of lattices]. Describe the theory map relative to an appropriate $H$.
