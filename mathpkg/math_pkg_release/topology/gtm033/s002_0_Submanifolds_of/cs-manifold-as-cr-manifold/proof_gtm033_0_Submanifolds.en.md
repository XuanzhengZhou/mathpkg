---
role: proof
locale: en
of_concept: cs-manifold-as-cr-manifold
source_book: gtm033
source_chapter: "0"
source_section: "Submanifolds of R^{n+k}"
---

# Proof of $C^s$ Manifold as a $C^r$ Manifold

Let $\alpha$ be a $C^s$ differential structure on a topological space $M$, i.e., a maximal $C^s$ atlas. Let $r$ be an integer with $1 \leqslant r < s$ (the case $r = 0$ reduces to the underlying topological manifold, which is trivially handled).

Since $\alpha$ is a $C^s$ atlas, for any two charts $(\varphi, U), (\psi, V) \in \alpha$, the transition maps

$$\psi \circ \varphi^{-1} : \varphi(U \cap V) \to \psi(U \cap V), \qquad
\varphi \circ \psi^{-1} : \psi(U \cap V) \to \varphi(U \cap V)$$

are of class $C^s$ on the open sets $\varphi(U \cap V)$ and $\psi(U \cap V)$, respectively.

Every $C^s$ map between open subsets of Euclidean space is in particular a $C^r$ map, since differentiability of order $s$ implies differentiability of all lower orders $r < s$. Therefore the same transition maps are also of class $C^r$. This means $\alpha$ itself is a $C^r$ atlas, though not necessarily maximal as a $C^r$ atlas.

By the proposition that every $C^r$ atlas is contained in a unique maximal $C^r$ atlas, there exists a unique $C^r$ differential structure $\alpha_r$ on $M$ that contains $\alpha$. Explicitly,

$$\alpha_r = \{ (\theta, W) \mid (\theta, W) \text{ is a chart on } M \text{ having } C^r \text{ overlap with every chart in } \alpha \}.$$

Thus every $C^s$ manifold $(M, \alpha)$ determines a canonical $C^r$ manifold $(M, \alpha_r)$ for each $1 \leqslant r < s$. In categorical terms, this construction defines a forgetful functor from the category of $C^s$ manifolds to the category of $C^r$ manifolds.

Note that $\alpha_r$ may properly contain $\alpha$: there may be charts whose overlap with all $C^s$ charts is merely $C^r$ but not $C^s$. Hence a $C^s$ structure and the induced $C^r$ structure are distinct objects in general. The converse — whether every $C^r$ manifold admits a compatible $C^s$ structure for $s > r$ — is a subtle problem (see Chapter 2 for the affirmative answer when $r \geqslant 1$). $\square$
