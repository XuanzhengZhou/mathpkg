---
role: proof
locale: en
of_concept: residual-normal-crossing
source_book: gtm014
source_chapter: "VI"
source_section: "5. The Thom-Boardman Stratification"
---

**Proof of Proposition 5.6.**

Consider the target map
$$\beta: T_1 \times \cdots \times T_s \to Y \times \cdots \times Y \quad (s\text{ copies})$$
defined by taking the product of the individual target maps $T_j \to Y$. Since each $T_j \to Y$ is a submersion, the product map $\beta$ is also a submersion.

Let $\Delta_s(Y) \subset Y \times \cdots \times Y$ denote the (multi-)diagonal. The condition that distinct points $x_1,\ldots,x_s \in X$ with $x_j \in T_j(f)$ satisfy $f(x_1) = \cdots = f(x_s) = y$ is equivalent to the condition that the $s$-tuple $(j^k f(x_1),\ldots,j^k f(x_s))$ lies in $\beta^{-1}(\Delta_s(Y))$.

One then applies the multijet transversality theorem (an extension of the Thom transversality theorem to the multijet bundle ${}_sJ^k(X,Y)$) to the submanifold $\beta^{-1}(\Delta_s(Y))$ of $T_1 \times \cdots \times T_s$. Since $\beta$ is a submersion, $\beta^{-1}(\Delta_s(Y))$ is a submanifold of $T_1 \times \cdots \times T_s$. The transversality of the $s$-fold $k$-jet $j^k_s f$ to $\beta^{-1}(\Delta_s(Y))$ is precisely equivalent to the generalized normal crossing condition (5.5): it ensures that at any $s$-tuple of distinct points mapping to the same $y$, the images $(df)_{x_j}H_j$ of the tangent spaces $H_j = T_{x_j}(T_j(f))$ are in general position in $T_y Y$.

By the parametrized transversality theorem (or the multijet transversality theorem), the set of maps $f$ whose $s$-fold $k$-jet is transversal to $\beta^{-1}(\Delta_s(Y))$ is residual in $C^\infty(X,Y)$. This proves that the generalized normal crossing condition holds for a residual set of maps.

Theorem 5.2 follows immediately as the special case where $T_j = S_{I_j}$ (the universal Boardman subbundles), since the target maps $S_{I_j} \to Y$ are submersions by Boardman's theorem.
