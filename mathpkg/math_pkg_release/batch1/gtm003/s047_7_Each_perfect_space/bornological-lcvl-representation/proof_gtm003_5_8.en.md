---
role: proof
locale: en
of_concept: bornological-lcvl-representation
source_book: gtm003
source_chapter: "V: Order Structures"
source_section: "8. Stone-Weierstrass and Representation Theorems"
---

In view of (5.5) and (6.4), the assumption that $(E, \mathfrak{T})$ be bornological implies that $\mathfrak{T}$ is the order topology $\mathfrak{T}_O$. Hence by (6.3), $(E, \mathfrak{T})$ is the inductive limit of the subspaces $(E_\alpha, p_\alpha)$ ($\alpha \in \mathbf{A}$) where
$$
E_\alpha = \bigcup_{n=1}^{\infty} n[-a_\alpha, a_\alpha],
$$
$p_\alpha$ is the gauge of $[-a_\alpha, a_\alpha]$ on $E_\alpha$, and $\{a_\alpha : \alpha \in \mathbf{A}\}$ is a directed subset of the positive cone of $E$ such that $\bigcup_\alpha E_\alpha = E$.

By (6.2), each $(E_\alpha, p_\alpha)$ is a Banach lattice, and by (8.4) even an (AM)-space with unit $a_\alpha$. Hence by (8.5), each $(E_\alpha, p_\alpha)$ can be identified with $\mathcal{C}_{\mathbb{R}}(X_\alpha)$ for a suitable compact space $X_\alpha$. The assertion then follows from the definition of inductive topologies (Chapter II, Section 6): $\mathfrak{T}$ is the finest locally convex topology on $E$ making each inclusion $f_\alpha : \mathcal{C}_{\mathbb{R}}(X_\alpha) \hookrightarrow E$ continuous.
