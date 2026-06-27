---
role: proof
locale: en
of_concept: canonical-decomposition-of-linear-map
source_book: gtm003
source_chapter: "III"
source_section: "1"
---

Given a linear map $u: L \to M$, let $N = u^{-1}(0)$. Define $\phi: L \to L/N$ as the canonical quotient map sending each $x \in L$ to its equivalence class $\hat{x} = x + N$. Define $u_0: L/N \to u(L)$ by $u_0(\hat{x}) = u(x)$; this is well-defined since $u$ is constant on each coset of $N$, and it is bijective by construction (each element of $u(L)$ is $u(x)$ for some $x$, corresponding uniquely to $\hat{x}$). Finally, $\psi: u(L) \to M$ is the canonical inclusion. Then for any $x \in L$, $(\psi \circ u_0 \circ \phi)(x) = \psi(u_0(\hat{x})) = \psi(u(x)) = u(x)$, so $u = \psi \circ u_0 \circ \phi$.

The map $u_0$ is an algebraic isomorphism: it is linear because $u_0(\alpha \hat{x} + \beta \hat{y}) = u(\alpha x + \beta y) = \alpha u(x) + \beta u(y) = \alpha u_0(\hat{x}) + \beta u_0(\hat{y})$, injective by definition of $N$, and surjective onto $u(L)$ by construction.
