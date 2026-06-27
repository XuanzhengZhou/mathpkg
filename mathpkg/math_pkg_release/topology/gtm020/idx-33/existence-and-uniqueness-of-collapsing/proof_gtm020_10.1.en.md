---
role: proof
locale: en
of_concept: existence-and-uniqueness-of-collapsing
source_book: gtm020
source_chapter: "10. Relative K-Theory"
source_section: "1. Collapsing of Trivialized Bundles"
---

**Proof.** If the quotient $(\xi/t, u, r)$ exists, there are a local coordinate chart $(V, \phi)$, where $* \in V$, and a map $\phi: V \times F^n \rightarrow (\xi/t)|V$ such that $r$ is the restriction of $\phi^{-1}$ to the fibre of $\xi/t$ over $*$. Let $t' = \phi^{-1}u$ on $\xi$ over $p_A^{-1}(V) = U$. This construction demonstrates also the last statement of the proposition.

Conversely, we construct $E(\xi/t)$ as the quotient of $E(\xi)$ where $x$ and $x'$ are identified provided $t(x) = t(x')$. There are no further identifications, and $E(\xi/t) \rightarrow X/A$ with the induced projection is a bundle of vector spaces. Let $u: \xi \rightarrow \xi/t$ be the quotient map. It is a fibrewise linear isomorphism. The prolongation $t'$ of $t$ defines a trivialization of $\xi/t$ on $p_A(V)$, and $\xi/t$ is locally trivial at $*$. The coordinate charts of $\xi$ away from $A$ provide local trivializations of $\xi/t$ away from the basepoint $*$. The isomorphism $r$ is determined by the local trivialization at $*$.

For uniqueness, the commutative diagram defines $v$ uniquely as $v = u' \circ u^{-1}$ (since $u$ is a fibrewise isomorphism). The compatibility with the basepoint isomorphisms $r$ and $r'$ follows from the condition $t = ru|_{E(\xi|A)} = r'u'|_{E(\xi|A)}$. Since $u$ and $u'$ are isomorphisms away from $A$, $v$ is an isomorphism there; at the basepoint, the compatibility condition ensures $v_*$ is an isomorphism as well. Thus $v$ is a global isomorphism of vector bundles.

For the final statement, given a vector bundle $\eta$ over $X/A$, choose a local trivialization near the basepoint $*$, giving a trivialization $t$ of $\eta$ on a neighborhood $V$ of $*$. Pull back $\eta$ to $X$ via the quotient map $p_A: X \rightarrow X/A$, giving $\xi = p_A^*(\eta)$, and the trivialization pulls back to a trivialization over $p_A^{-1}(V) = U$. Then $\xi/t \cong \eta$ by construction.
