---
role: proof
locale: en
of_concept: pseudo-metric-quotient
source_book: gtm027
source_chapter: "4"
source_section: "Existence of Continuous Functions"
---

# Proof of Pseudo-metric to Metric Quotient

**Theorem 15.** Let $(X,d)$ be a pseudo-metric space, let $\mathfrak{D}$ be the family of all sets $\{x\}^{-}$ for $x$ in $X$, and for members $A$ and $B$ of $\mathfrak{D}$ let $\rho(A,B) = \operatorname{dist}(A,B)$. Then $(\mathfrak{D}, \rho)$ is a metric space.

The projection of $X$ onto $\mathfrak{D}$ is an open map relative to the quotient topology for $\mathfrak{D}$, and the quotient topology coincides with the metric topology derived from $\rho$.

*Proof.* First, $\{x\}^{-}$ is precisely the set of all points $y$ such that $d(x,y) = 0$ (by Theorem 9), and the decomposition $\mathfrak{D}$ is the quotient $X/R$ where $R$ is the equivalence relation $\{(x,y) : d(x,y) = 0\}$.

To verify that $\rho$ is a metric on $\mathfrak{D}$: Clearly $\rho(A,B) \geq 0$ and $\rho(A,B) = \rho(B,A)$. If $\rho(A,B) = 0$, then $\inf\{d(x,y) : x \in A, y \in B\} = 0$. Since $A = \{x\}^{-}$ and $B = \{y\}^{-}$ for some $x, y$, and $d$ is zero exactly on pairs belonging to $R$, we must have $A = B$. The triangle inequality $\rho(A,C) \leq \rho(A,B) + \rho(B,C)$ follows from the triangle inequality for $d$.

The projection $\pi: X \to \mathfrak{D}$ given by $\pi(x) = \{x\}^{-}$ is continuous because $\rho(\pi(x), \pi(y)) \leq d(x,y)$. Since the image under $\pi$ of an open $r$-sphere in $X$ is an open $r$-sphere in $\mathfrak{D}$, $\pi$ is an open map relative to the metric topology on $\mathfrak{D}$. By Theorem 3.10, the projection is also open relative to the quotient topology, and by Theorem 3.8 these two topologies coincide.

