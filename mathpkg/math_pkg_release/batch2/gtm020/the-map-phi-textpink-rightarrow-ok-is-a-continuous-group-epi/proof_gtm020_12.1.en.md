---
locale: en
of_concept: the-map-phi-textpink-rightarrow-ok-is-a-continuous-group-epi
role: proof
source_book: gtm020
source_chapter: 12. Clifford Algebras
source_section: '1'
---

Clearly, $\phi$ is continuous, and the relation $\phi(uv)x = uvx(uv)^* = uvxv^*u^* = u(\phi(v)x)u^* = \phi(u)\phi(v)x$ yields the group morphism property of $\phi$.

To prove $\phi$ is surjective, we begin by proving that $\phi(u)$ for $u \in S^{n-1}$ is a reflection through the hyperplane perpendicular to $u$. Let $x = tu + u'$, where $(u|u') = 0$. Then $\phi(u)x = u(tu + u')u^* = tuuu^* + uu'u^* = -tu - u'uu^* = -tu + u'$. This proves the statement about $\phi(u)$ for $u \in S^{k-1}$. Since these reflections generate $O(k)$, the map $\phi$ is surjective.

For $u \in S^{n-1}$, $\det \phi(u) = -1$ and $\det \phi(u_1 \cdots u_r) = (-1)^r$ for $u_i \in S^{n-1}$ and $1 \leq i \leq r$. Therefore, $u \in \text{Spin}(k)$ if and only if $\phi(u) \in SO(k)$.

For $u \in \text{ker} \phi$ we have $ue_i u^* = e_i$, or $ue_i = e_i u$ since $uu^* =
