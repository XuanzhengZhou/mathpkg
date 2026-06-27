---
role: proof
locale: en
of_concept: positive-linear-functional-kx-continuity
source_book: gtm036
source_chapter: "4"
source_section: "I (Complex Measures)"
---
Suppose first that the scalars are real and let $\phi \in (K(X))^*$. For each $f \geq 0$, put
$$\phi^+(f) = \sup \{ \phi(g): 0 \leq g \leq f \};$$
then if $f \in K(X)$, $\phi^+(f) < \infty$, by the continuity of $\phi$. Both $\phi^+$ and $\phi^-$ can be extended to give positive linear functionals on $K(X)$.

Conversely, let $\phi$ be a positive linear functional on $K(X)$. Then for each compact set $C \subset X$, the restriction of $\phi$ to $K(C)$ (the subspace of functions with support in $C$) is bounded on order-bounded subsets. Since the inductive limit topology $\mathcal{T}$ is the finest locally convex topology making the injections $K(C) \to K(X)$ continuous, it follows that $\phi$ is $\mathcal{T}$-continuous.

For complex scalars, consider the real and imaginary parts of $\phi$ acting on the real subspace of $K(X)$ consisting of the real valued functions.
