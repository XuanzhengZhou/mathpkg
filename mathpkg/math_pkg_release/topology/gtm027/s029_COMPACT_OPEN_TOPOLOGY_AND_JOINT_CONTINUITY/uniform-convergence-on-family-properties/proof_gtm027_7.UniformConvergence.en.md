---
role: proof
locale: en
of_concept: uniform-convergence-on-family-properties
source_book: gtm027
source_chapter: "7"
source_section: "Uniform Convergence"
---

# Proof of Theorem 7.10 — Properties of Uniform Convergence on a Family of Sets

Let $F$ be a family of functions on $X$ to a uniform space $(Y, \mathcal{V})$, $\alpha$ a family of subsets of $X$, and $G$ the space of all functions on $X$ to $Y$ which are continuous on each member of $\alpha$. The uniformity $\mathcal{U} \mid \alpha$ of uniform convergence on members of $\alpha$ is the coarsest uniformity making the restriction maps $F \to (F|_A, \text{u.c.})$ uniformly continuous for each $A \in \alpha$.

**(a)** For each $A \in \alpha$, the uniformity of uniform convergence on $A$ is larger than pointwise convergence on $A$ (each point is a singleton subset) and smaller than uniform convergence on $X$ (since $A \subset X$). Taking the supremum over $A \in \alpha$ preserves these comparisons. Hence $\mathcal{U} \mid \alpha$ lies between the pointwise uniformity and the full u.c. uniformity.

**(b)** A net $\{f_n\}$ converges to $g$ in the topology of $\mathcal{U} \mid \alpha$ iff it converges uniformly on each $A \in \alpha$. By Theorem 7.8(b), uniform convergence on $A$ is equivalent to being Cauchy on $A$ plus pointwise convergence on $A$. Taking all $A \in \alpha$ yields the result.

**(c)** If $(Y, \mathcal{V})$ is complete, then for each $A \in \alpha$, the space of all functions on $A$ to $Y$ is complete in the u.c. uniformity (Theorem 7.8(c)). A Cauchy net in $\mathcal{U} \mid \alpha$ is Cauchy on each $A$, hence converges uniformly on each $A$ to a limit function. The limit function is in $G$ because continuity on each $A$ is preserved under uniform limits.

**(d)** By (a) of Theorem 7.9, the set of functions continuous on a given $A$ is closed under uniform convergence on $A$. Hence $F$ is closed in $G$ relative to $\mathcal{U} \mid \alpha$. If $(Y, \mathcal{V})$ is complete, then $G$ is complete by (c), so the closed subset $F$ is also complete.

**(e)** For each $A \in \alpha$, uniform convergence on $A$ is jointly continuous on $A$ by Theorem 7.9(b). Since $\mathcal{U} \mid \alpha$ induces a topology finer than uniform convergence on each $A$, it is jointly continuous on each $A \in \alpha$.
