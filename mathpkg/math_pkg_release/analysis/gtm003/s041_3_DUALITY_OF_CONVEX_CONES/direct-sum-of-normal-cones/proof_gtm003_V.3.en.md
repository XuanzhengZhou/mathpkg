---
role: proof
locale: en
of_concept: direct-sum-of-normal-cones
source_book: gtm003
source_chapter: "V"
source_section: "3"
---

\noindent\textbf{Necessity.} Each $L_\alpha$ can be identified with a subspace of $L = \bigoplus_\alpha L_\alpha$ via the canonical embedding. Under this identification, $C_\alpha = L_\alpha \cap C$. Since the restriction of a normal cone to a subspace is normal (the subspace topology renders $C_\alpha$ normal in $L_\alpha$ if $C$ is normal in $L$), the condition is necessary.

\medskip
\noindent\textbf{Sufficiency.} Assume that each $C_\alpha$ is normal in $L_\alpha$. By passing to the underlying real space if necessary, we may assume $K = \mathbb{R}$.

Let $\mathfrak{V}_\alpha$ be a neighborhood base of $0$ in $L_\alpha$ satisfying condition (d) of Theorem 3.1; that is, each $V_\alpha \in \mathfrak{V}_\alpha$ is convex, circled, and $C_\alpha$-saturated, i.e., $[V_\alpha \cap C_\alpha] \subset V_\alpha$.

A neighborhood base of $0$ in the locally convex direct sum $L = \bigoplus_\alpha L_\alpha$ is given by the family of all sets
$$V = \prod_\alpha V_\alpha \quad (V_\alpha \in \mathfrak{V}_\alpha, \; \alpha \in \mathbf{A})$$
where only finitely many $V_\alpha$ differ from $L_\alpha$. (More precisely, these are taken under the canonical identification with subsets of the direct sum.)

Now consider $[V \cap C]$, the $C$-saturated hull. Since $C = \bigoplus_\alpha C_\alpha$, we have $V \cap C = \bigcup_\alpha (V_\alpha \cap C_\alpha)$ (identifying each summand). The $C$-saturated hull of this set is precisely the convex hull of $\bigcup_\alpha [V_\alpha \cap C_\alpha]$. Since each $V_\alpha$ is $C_\alpha$-saturated, we have $[V_\alpha \cap C_\alpha] \subset V_\alpha$ for every $\alpha$.

Therefore, $[V \cap C]$ is contained in the convex hull of $\bigcup_\alpha V_\alpha$, which is a subset of $V$ because $V$ (as a product of convex sets under the direct sum topology) is convex. Consequently, $[V \cap C] \subset V$ for all $V$ in the neighborhood base.

By Theorem 3.1 (c), this implies that $C$ is normal in $L$.
