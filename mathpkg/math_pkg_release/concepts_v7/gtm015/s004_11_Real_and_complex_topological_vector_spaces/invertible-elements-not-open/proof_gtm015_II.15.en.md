---
role: proof
locale: en
of_concept: invertible-elements-not-open
source_book: gtm015
source_chapter: "Chapter 2 – Topological Vector Spaces"
source_section: "15. The space (S)"
---

# Proof that Invertible Elements are Not Open

**Theorem (15.11).** If $\mu$ is totally finite and assumes arbitrarily small values, then the group of invertible elements in $[\mathcal{M}]$ is not an open set in $[\mathcal{M}]$.

*Proof.* Let $G$ be the group of invertible elements. Assume to the contrary that $G$ is open in $[\mathcal{M}]$. Then there exists a neighborhood $V$ of $1 = [1]$ (the multiplicative identity) contained in $G$. By translation invariance, $V - 1$ is a neighborhood of $\theta$.

By (15.8), since $\mu$ assumes arbitrarily small values, the neighborhood $V - 1$ contains an entire line through some nonzero $u = [f]$; that is, $\{\alpha u : \alpha \in \mathbb{R}\} \subset V - 1$, so $1 + \alpha u \in V \subset G$ for all $\alpha \in \mathbb{R}$.

Since $u \neq \theta$, there exists a measurable set $E$ with $\mu(E) > 0$ on which $f$ does not vanish a.e. Choose $\alpha$ such that $\alpha f(x) = -1$ on a set of positive measure. Then $1 + \alpha u = [1 + \alpha f]$ vanishes on a set of positive measure, hence is not invertible (an element $[g]$ is invertible iff $g$ is nonzero a.e.), contradicting $1 + \alpha u \in G$. Thus $G$ cannot be open. $\square$
