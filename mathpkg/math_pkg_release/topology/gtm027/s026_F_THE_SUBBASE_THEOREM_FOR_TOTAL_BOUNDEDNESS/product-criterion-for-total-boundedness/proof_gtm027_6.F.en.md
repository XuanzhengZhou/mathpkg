---
role: proof
locale: en
of_concept: product-criterion-for-total-boundedness
source_book: gtm027
source_chapter: "6"
source_section: "F"
---

# Proof of Product Criterion for Total Boundedness

Let $\{(X_\alpha, \mathfrak{u}_\alpha)\}_{\alpha \in \Lambda}$ be a family of uniform spaces and let $X = \prod_{\alpha} X_\alpha$ be their product with the product uniformity $\mathfrak{u}$.

**($\Leftarrow$)** Suppose each coordinate space $(X_\alpha, \mathfrak{u}_\alpha)$ is totally bounded. The product uniformity $\mathfrak{u}$ has as a subbase the family
$$
\mathcal{S} = \left\{ \{(x,y) \in X \times X : (x_\alpha, y_\alpha) \in U_\alpha\} \;\middle|\; \alpha \in \Lambda,\; U_\alpha \in \mathfrak{u}_\alpha \right\}.
$$
For any such subbasic entourage determined by $\alpha$ and $U_\alpha$, total boundedness of $(X_\alpha, \mathfrak{u}_\alpha)$ yields a finite cover $\{A_1, \dots, A_n\}$ of $X_\alpha$ with $A_i \times A_i \subset U_\alpha$ for each $i$. Lifting this cover to $X$ by taking $B_i = \pi_\alpha^{-1}(A_i)$, where $\pi_\alpha : X \to X_\alpha$ is the projection, gives a finite cover of $X$ with $B_i \times B_i$ contained in the subbasic entourage determined by $U_\alpha$. By the Subbase Theorem for Total Boundedness, $(X, \mathfrak{u})$ is totally bounded.

**($\Rightarrow$)** Suppose $(X, \mathfrak{u})$ is totally bounded. For each $\alpha \in \Lambda$, the projection $\pi_\alpha : X \to X_\alpha$ is uniformly continuous. Given any $U_\alpha \in \mathfrak{u}_\alpha$, the preimage under the product map $(\pi_\alpha \times \pi_\alpha)^{-1}(U_\alpha)$ is an entourage in $\mathfrak{u}$. By total boundedness of $X$, there is a finite cover $\{C_1, \dots, C_k\}$ of $X$ such that $C_j \times C_j \subset (\pi_\alpha \times \pi_\alpha)^{-1}(U_\alpha)$ for each $j$. Applying $\pi_\alpha$ yields $\pi_\alpha(C_j) \times \pi_\alpha(C_j) \subset U_\alpha$, and $\{\pi_\alpha(C_1), \dots, \pi_\alpha(C_k)\}$ is a finite cover of $X_\alpha$. Thus $(X_\alpha, \mathfrak{u}_\alpha)$ is totally bounded. $\square$
