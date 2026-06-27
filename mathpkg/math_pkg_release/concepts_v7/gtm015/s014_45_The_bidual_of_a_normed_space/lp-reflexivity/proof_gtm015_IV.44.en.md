---
role: proof
locale: en
of_concept: lp-reflexivity
source_book: gtm015
source_chapter: "IV"
source_section: "44"
---

# Proof of Reflexivity of $L^p$ Spaces

**Case $1 < p < \infty$:** Let $(X, \mathcal{M}, \mu)$ be a measure space and let $1 < p < \infty$. The dual of $L^p(\mu)$ is isometrically isomorphic to $L^q(\mu)$, where $1/p + 1/q = 1$ (this is the Riesz representation theorem for $L^p$ spaces; see Section 39).

The dual of $L^q(\mu)$ is isometrically isomorphic to $L^p(\mu)$ (since $1/q + 1/p = 1$). The canonical embedding $J: L^p \to (L^p)'' = (L^q)'$ composed with these isomorphisms yields the identity map on $L^p$, so $J$ is surjective. Therefore $L^p$ is reflexive.

More precisely: Let $\Phi_p: L^q \to (L^p)'$ be the isometric isomorphism given by $\Phi_p(g)(f) = \int f g \, d\mu$ for $f \in L^p$, $g \in L^q$. Let $\Phi_q: L^p \to (L^q)'$ be the analogous isomorphism. The bidual map $(L^p)'' \to L^p$ given by composing $(\Phi_p)^{-1} \circ \Phi_p^*$ with the inverse of $\Phi_q$ yields the identity, proving surjectivity of the canonical embedding. Thus $L^p$ is reflexive.

**Case $p = 1$:** The space $\ell^1$ is not reflexive. Its dual is $\ell^\infty$, and the dual of $\ell^\infty$ is the space of finitely additive measures on $\mathbb{N}$, which is strictly larger than $\ell^1$ under the canonical embedding. More concretely, the element of $(\ell^\infty)'$ given by a Banach limit (which extends the ordinary limit functional from the space of convergent sequences) does not correspond to any element of $\ell^1$. Therefore the canonical embedding $\ell^1 \to (\ell^1)''$ is not surjective. $\square$
