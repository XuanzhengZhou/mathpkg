---
role: proof
locale: en
of_concept: topological-homomorphism-via-bijective-map
source_book: gtm003
source_chapter: "III"
source_section: "1"
---

If $u_0$ is an isomorphism, then $u_0$ is a homeomorphism, hence open. Since $\phi$ is open (quotient map) and $\psi$ is an embedding (open onto its image), the composition $u = \psi \circ u_0 \circ \phi$ is open onto $u(L)$, i.e., $u$ is a topological homomorphism.

Conversely, if $u$ is a topological homomorphism, then $u$ is open onto $u(L)$. For any open set $G \subset L$, $\phi(G)$ is open in $L/N$, and $u(G) = \psi(u_0(\phi(G)))$ is open in $u(L)$. Since $\psi$ is an embedding, $u_0(\phi(G))$ must be open in $u(L)$. As $\phi$ is surjective, this means $u_0$ maps open sets to open sets. Since $u_0$ is bijective and continuous (both $\phi$ and $u$ are continuous, and $u(L)$ carries the induced topology), $u_0^{-1}$ is continuous, hence $u_0$ is an isomorphism.
