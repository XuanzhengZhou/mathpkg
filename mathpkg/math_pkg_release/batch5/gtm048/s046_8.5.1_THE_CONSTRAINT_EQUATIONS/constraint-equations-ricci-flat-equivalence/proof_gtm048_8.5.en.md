---
role: proof
locale: en
of_concept: constraint-equations-ricci-flat-equivalence
source_book: gtm048
source_chapter: "8"
source_section: "8.5.1"
---

**Proof of (a) $\Rightarrow$ (b):** Suppose $(M,g)$ is Ricci flat, $\operatorname{Ric}(g) = 0$. Let $\beta: B \to M$ be a spacelike imbedding with second fundamental form $k$ and induced metric $b = \beta^* g$. Let $\tilde{k}$ be the $(1,1)$-tensor physically equivalent to $k$ via $b$.

The Gauss equation relates the intrinsic curvature of $(B,b)$ to the ambient curvature and the second fundamental form. In terms of the Riemann curvature tensors, for vector fields $X,Y,Z,W$ tangent to $B$:

$$
R_b(X,Y,Z,W) = R_g(X,Y,Z,W) + \langle k(X,Z), k(Y,W) \rangle - \langle k(X,W), k(Y,Z) \rangle.
$$

Taking traces (contracting with the inverse metric $b^{-1}$) yields the scalar Gauss equation. Since the ambient Ricci tensor vanishes and the spacetime has dimension 4 while the hypersurface has dimension 3, the double trace of the ambient Riemann tensor decomposes as:

$$
s = (\operatorname{tr} \tilde{k})^2 - \operatorname{tr}(\tilde{k} \circ \tilde{k}),
$$

where $s$ is the scalar curvature of $(B,b)$. This is the first (Hamiltonian) constraint equation.

The Codazzi equation relates the covariant derivative of the second fundamental form to the ambient Ricci tensor projected onto the hypersurface. For a Ricci-flat ambient spacetime, the Codazzi equation reduces to:

$$
\operatorname{div} \tilde{k} = d(\operatorname{tr} \tilde{k}),
$$

where the divergence is taken with respect to the Levi-Civita connection of $b$. This is the second (momentum) constraint equation.

**Proof of (b) $\Rightarrow$ (a):** Conversely, suppose that for every spacelike imbedding $\beta: B \to M$, the triple $(B, b, \tilde{k})$ satisfies both constraint equations. Fix a point $p \in M$ and a unit timelike vector $n \in T_p M$, $\langle n, n \rangle = -1$. Let $B_p$ be the spacelike hypersurface through $p$ orthogonal to $n$, and let $\beta$ be the inclusion. Near $p$, the Gauss-Codazzi equations express the components of $\operatorname{Ric}(g)$ in terms of the scalar curvature $s$, the second fundamental form $\tilde{k}$, and their derivatives along $B_p$. The two constraint equations imply that the projections $\operatorname{Ric}(g)(n, n)$ and $\operatorname{Ric}(g)(n, X)$ (for $X$ tangent to $B_p$) both vanish. Since this holds for every choice of unit timelike $n$ at every $p \in M$, all components of $\operatorname{Ric}(g)$ vanish, so $\operatorname{Ric}(g) = 0$.
