---
role: proof
locale: en
of_concept: embedding-of-completions-under-different-topologies
source_book: gtm036
source_chapter: ""
source_section: ""
---

The identity map $\iota: (E, \mathcal{U}) \to (E, \mathcal{T})$ is continuous since $\mathcal{U}$ is stronger than $\mathcal{T}$. By the universal property of completions, $\iota$ extends uniquely to a continuous linear map $\iota^\wedge: (E, \mathcal{U})^\wedge \to (E, \mathcal{T})^\wedge$.

The embedding condition holds precisely when $\iota^\wedge$ is injective. By the injectivity criterion for completion maps, $\iota^\wedge$ is injective if and only if whenever $\{x_\gamma\}$ is a $\mathcal{U}$-Cauchy net and $\iota(x_\gamma) \to \iota(x_0)$ in $\mathcal{T}$, we have $x_\gamma \to x_0$ in $\mathcal{U}$. Since $\iota$ is the identity, this means: every $\mathcal{U}$-Cauchy net that $\mathcal{T}$-converges to some limit must $\mathcal{U}$-converge to the same limit.

For the sufficient condition: if there is a local base of $\mathcal{T}$-closed $\mathcal{U}$-neighborhoods of $0$, then any $\mathcal{U}$-Cauchy net $\{x_\gamma\}$ that $\mathcal{T}$-converges to $x_0$ must also $\mathcal{U}$-converge to $x_0$, because the $\mathcal{T}$-closed $\mathcal{U}$-neighborhoods force the convergence in $\mathcal{U}$.
