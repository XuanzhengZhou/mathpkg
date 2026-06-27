---
role: proof
locale: en
of_concept: homology-functor
source_book: gtm004
source_chapter: "IV. Derived Functors"
source_section: "1. Complexes"
---

# Proof of The Homology Functor

Let $C = \{C_n, \partial_n^C\}$ and $D = \{D_n, \partial_n^D\}$ be chain complexes over $\Lambda$,
and let $\varphi: C \to D$ be a chain map. We need to verify the functoriality axioms.

**Well-definedness on objects.** For each $n \in \mathbb{Z}$, we have
$$H_n(C) = \ker \partial_n^C \,/\, \operatorname{im} \partial_{n+1}^C.$$
Since $\partial^C \partial^C = 0$, we have $\operatorname{im} \partial_{n+1}^C \subseteq \ker \partial_n^C$, so the quotient is well-defined.

**Well-definedness on morphisms.** A chain map $\varphi: C \to D$ satisfies $\varphi_{n-1} \partial_n^C = \partial_n^D \varphi_n$ for all $n$.
If $x \in \ker \partial_n^C$, then
$$\partial_n^D(\varphi_n(x)) = \varphi_{n-1}(\partial_n^C(x)) = \varphi_{n-1}(0) = 0,$$
so $\varphi_n(x) \in \ker \partial_n^D$.
If $x \in \operatorname{im} \partial_{n+1}^C$, say $x = \partial_{n+1}^C(y)$, then
$$\varphi_n(x) = \varphi_n(\partial_{n+1}^C(y)) = \partial_{n+1}^D(\varphi_{n+1}(y)) \in \operatorname{im} \partial_{n+1}^D.$$
Thus $\varphi_n$ maps $\ker \partial_n^C$ into $\ker \partial_n^D$ and $\operatorname{im} \partial_{n+1}^C$ into $\operatorname{im} \partial_{n+1}^D$.
Consequently, $\varphi$ induces a well-defined morphism
$$H_n(\varphi): H_n(C) \to H_n(D), \qquad [x] \mapsto [\varphi_n(x)],$$
of degree zero on the homology modules.
The collection $H(\varphi) = \{H_n(\varphi)\}_{n \in \mathbb{Z}}$ defines a morphism of graded modules $H(C) \to H(D)$.

**Functoriality.** For the identity chain map $\operatorname{id}_C: C \to C$, we have
$$H_n(\operatorname{id}_C)([x]) = [\operatorname{id}_{C_n}(x)] = [x],$$
so $H(\operatorname{id}_C) = \operatorname{id}_{H(C)}$.

Given composable chain maps $\varphi: C \to D$ and $\psi: D \to E$, we compute
$$H_n(\psi \circ \varphi)([x]) = [(\psi_n \circ \varphi_n)(x)] = [\psi_n(\varphi_n(x))] = H_n(\psi)([\varphi_n(x)]) = H_n(\psi)(H_n(\varphi)([x])),$$
so $H_n(\psi \circ \varphi) = H_n(\psi) \circ H_n(\varphi)$ for each $n$, and hence
$$H(\psi \circ \varphi) = H(\psi) \circ H(\varphi).$$

Therefore $H(-)$ is a covariant functor from the category of chain complexes over $\Lambda$ to the category of graded $\Lambda$-modules.
Each $H_n(-)$ is likewise a functor into $\mathfrak{M}_\Lambda$.
