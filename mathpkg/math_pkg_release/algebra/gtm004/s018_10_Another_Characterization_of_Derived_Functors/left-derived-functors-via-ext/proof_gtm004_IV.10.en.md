---
role: proof
locale: en
of_concept: left-derived-functors-via-ext
source_book: gtm004
source_chapter: "IV"
source_section: "10. Another Characterization of Derived Functors"
---

# Proof of Characterization of Left Derived Functors via Ext

**Corollary 10.2.** Let $T : \mathfrak{M}_\Lambda \to \mathfrak{Ab}$ be a right exact functor and let $A$ be a $\Lambda$-module. Then there are natural isomorphisms

$$\Gamma : [\operatorname{Ext}_\Lambda^q(A, -), T] \xrightarrow{\cong} L_q T A, \qquad q = 0, 1, \dots.$$

**Proof.** By Theorem 10.1, we have natural isomorphisms

$$\Gamma : [\operatorname{Ext}_\Lambda^q(A, -), T] \xrightarrow{\cong} \tilde{L}_q T A$$

for any additive covariant functor $T$, where $\tilde{L}_q T A$ denotes the $q$-th left satellite of $T$ evaluated at $A$.

Since $T$ is right exact, the left satellites coincide with the left derived functors: $\tilde{L}_q T = L_q T$ for all $q \geq 0$. More precisely, for a right exact functor $T$, the left satellite $\tilde{L}_q T$ computed via a projective resolution of $A$ coincides with the $q$-th left derived functor $L_q T$, because both are defined as the homology of $T(P)$ where $P \to A$ is a projective resolution.

Therefore the isomorphisms of Theorem 10.1 specialize to

$$\Gamma : [\operatorname{Ext}_\Lambda^q(A, -), T] \xrightarrow{\cong} L_q T A, \qquad q = 0, 1, \dots,$$

as claimed. $\square$
