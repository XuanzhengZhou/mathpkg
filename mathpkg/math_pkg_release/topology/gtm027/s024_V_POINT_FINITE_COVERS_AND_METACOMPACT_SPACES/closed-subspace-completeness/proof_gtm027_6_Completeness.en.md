---
role: proof
locale: en
of_concept: closed-subspace-completeness
source_book: gtm027
source_chapter: "6"
source_section: "Completeness"
---

# Proof that Closed Subspaces of Complete Spaces are Complete (Theorem 6.22)

**Theorem 6.22.** A closed subspace of a complete space is complete, and a complete subspace of a Hausdorff uniform space is closed.

**Proof.** Let $(X, \mathcal{U})$ be a complete uniform space and let $Y \subset X$ be a closed subset with the relative uniformity.

If $\{y_n : n \in D\}$ is a Cauchy net in $Y$, then it is also a Cauchy net in $X$ (since the relative uniformity consists of intersections of members of $\mathcal{U}$ with $Y \times Y$). Since $X$ is complete, the net converges to some $x \in X$. Since $Y$ is closed in $X$, the limit $x$ must belong to $Y$ (a net in a closed set can only converge to points in that set). Therefore $Y$ is complete.

For the second statement: suppose $Y$ is a complete subspace of a Hausdorff uniform space $X$. Let $x \in \overline{Y}$. Then there exists a net $\{y_n\}$ in $Y$ converging to $x$ in $X$. By Theorem 6.21, this net is Cauchy in $X$, hence also Cauchy in $Y$ (relative uniformity). Since $Y$ is complete, the net converges to some $y \in Y$. But $X$ is Hausdorff and the net converges to both $x$ and $y$, so $x = y \in Y$. Thus $\overline{Y} = Y$, i.e., $Y$ is closed in $X$.
