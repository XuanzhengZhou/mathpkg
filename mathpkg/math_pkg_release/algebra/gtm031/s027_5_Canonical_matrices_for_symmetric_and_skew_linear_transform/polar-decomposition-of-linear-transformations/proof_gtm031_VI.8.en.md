---
role: proof
locale: en
of_concept: polar-decomposition-of-linear-transformations
source_book: gtm031
source_chapter: "VI"
source_section: "8"
---

**Case 1: $A$ is 1-1.** Form the positive definite transformation $B = AA'$ and let $P$ be its positive definite square root (Theorem 11). Set $O = P^{-1}A$. Then
$$OO' = P^{-1}AA'P^{-1} = P^{-1}BP^{-1} = P^{-1}P^2P^{-1} = 1,$$
which shows that $O$ is orthogonal. Since $A = PO$, the existence is established. Uniqueness: if $A = P_1 O_1$ with $P_1$ positive definite and $O_1$ orthogonal, then $AA' = P_1 O_1 O_1' P_1' = P_1^2$. By uniqueness of the positive definite square root, $P_1 = P$, and then $O_1 = P^{-1}A = O$.

**Case 2: General $A$.** Define $B = AA'$ and take $P$ to be the semi-definite square root of $B$. We define a mapping from $\mathfrak{S} = \mathfrak{R} P$ to $\mathfrak{S}_1 = \mathfrak{R} A$ by $xP \mapsto xA$. If $xP = yP$, then $(x - y)P = 0$ and so $(x - y)B = (x-y)P^2 = 0$. Since $B = AA'$, this implies $(x - y)AA' = 0$, so $(x - y)A = 0$, hence $xA = yA$. This shows the correspondence is single-valued. It is clearly linear.

This mapping preserves lengths: $(xA, xA) = (xAA', x) = (xB, x)$ and $(xP, xP) = (xP^2, x) = (xB, x)$.

Now $A$, $B$, and $P$ have the same null space, hence the same rank. It follows that the orthogonal complements $\mathfrak{S}^\perp$ and $\mathfrak{S}_1^\perp$ have the same dimension $h$. Let $(u_1, \ldots, u_h)$ and $(v_1, \ldots, v_h)$ be Cartesian bases of $\mathfrak{S}^\perp$ and $\mathfrak{S}_1^\perp$ respectively. Extend the isometry $xP \mapsto xA$ from $\mathfrak{S}$ to $\mathfrak{S}_1$ to an orthogonal transformation $O$ on all of $\mathfrak{R}$ by sending $u_i \mapsto v_i$. Then $A = PO$ as required.

$P$ is uniquely determined (as the semi-definite square root of $AA'$). $O$ is uniquely determined on $\mathfrak{S}$ but its action on $\mathfrak{S}^\perp$ is arbitrary up to an orthogonal transformation preserving the orthogonal complement; thus $O$ is unique if and only if $\mathfrak{S}^\perp = 0$, i.e., $A$ is 1-1.
