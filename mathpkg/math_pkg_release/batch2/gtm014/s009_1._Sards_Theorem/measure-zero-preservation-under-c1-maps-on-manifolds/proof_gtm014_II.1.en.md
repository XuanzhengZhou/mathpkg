---
role: proof
locale: en
of_concept: measure-zero-preservation-under-c1-maps-on-manifolds
source_book: gtm014
source_chapter: "II"
source_section: "§1. Sard's Theorem"
---

Let $\psi$ be a chart on $Y$ with domain $V$. Cover $f^{-1}(V)$ by a countable open covering $U_1, U_2, \ldots$ each of which is the domain for a chart $\phi_i: U_i \to \mathbf{R}^n$ and for which $f(U_i)$ is contained in $V$. Since $Z$ is of measure zero, $\phi_i(Z \cap U_i)$ has measure zero in $\mathbf{R}^n$.

Now $\psi \circ f \circ \phi_i^{-1}$ is $C^1$ on its domain in $\mathbf{R}^n$. By Proposition 1.3, $\psi \circ f \circ \phi_i^{-1}(\phi_i(Z \cap U_i)) = \psi(f(Z) \cap V \cap f(U_i))$ has measure zero in $\mathbf{R}^n$. Since this holds for each $i$, taking the union over $i$ shows that $\psi(f(Z) \cap V)$ is covered by countably many measure zero sets and thus has measure zero. Repeating this argument for a countable atlas of $Y$ yields that $f(Z)$ has measure zero in $Y$.
