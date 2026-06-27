---
role: proof
locale: en
of_concept: completion-of-separated-group
source_book: gtm018
source_chapter: "XII"
source_section: "62"
---

Let $\hat{X}$ be the completion of $X$ in its Weil topology; i.e., $\hat{X}$ is a locally compact group containing $X$ as a dense subgroup. Consider the class of all those subsets $\hat{E}$ of $\hat{X}$ for which $\hat{E} \cap X \in \mathbf{S}$. It is clear that this class is a $\sigma$-ring; in order to show that this $\sigma$-ring contains all Baire sets, we show that it contains a base for the topology of $\hat{X}$.

Suppose that $\hat{x}$ is any point of $\hat{X}$ and $\hat{U}$ is any neighborhood of $\hat{e}$ in $\hat{X}$; let $\hat{V}$ be a neighborhood of $\hat{e}$ such that $\hat{V}^{-1}\hat{V} \subset \hat{U}$. Since $\hat{V} \cap X$ is an open set in $X$, there exists a measurable open set $W$ in $X$ such that $W \subset \hat{V} \cap X$; since the topology of $X$ is the relative topology it inherits from $\hat{X}$, there exists an open set $\hat{W}$ in $\hat{X}$ such that $W = \hat{W} \cap X$. Without loss of generality, $\hat{W} \subset \hat{V}$. Since $X$ is dense in $\hat{X}$, there exists a point $x$ in $X$ such that $x \in \hat{x} \hat{W}^{-1}$; it follows that

$$\hat{x} \in x\hat{W} \subset \hat{x}\hat{W}^{-1}\hat{W} \subset \hat{x}\hat{V}^{-1}\hat{V} \subset \hat{x}\hat{U}.$$

Define $\hat{\mu}$ by writing $\hat{\mu}(\hat{E}) = \mu(\hat{E} \cap X)$ for every $\hat{E}$ in this $\sigma$-ring. This defines a Baire measure on $\hat{X}$ extending $\mu$.

To verify that $\hat{\mu}$ is well-defined and countably additive: if $\hat{E}_n$ are disjoint, then $\hat{E}_n \cap X$ are disjoint measurable sets in $X$, and $\hat{\mu}(\bigcup \hat{E}_n) = \mu(\bigcup (\hat{E}_n \cap X)) = \sum \mu(\hat{E}_n \cap X) = \sum \hat{\mu}(\hat{E}_n)$.
