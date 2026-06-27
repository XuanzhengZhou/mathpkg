---
role: proof
locale: en
of_concept: hom-functor-preserves-limits
source_book: gtm005
source_chapter: "V"
source_section: "4. Preservation of Limits"
---

**Proof.** Let $J$ be any category and $F : J \rightarrow C$ a functor with a limiting cone $v : b \rightarrow F$ in $C$. We must show that $C(c, v) : C(c, b) \rightarrow C(c, F-)$ is a limiting cone in $\mathbf{Set}$.

A cone $\tau : X \rightarrow C(c, F-)$ in $\mathbf{Set}$ with vertex a set $X$ assigns to each $j \in J$ a function $\tau_j : X \rightarrow C(c, Fj)$ such that for each arrow $u : i \rightarrow j$ in $J$, the diagram commutes:

$$\xymatrix{
X \ar[r]^{\tau_i} \ar[rd]_{\tau_j} & C(c, Fi) \ar[d]^{C(c, Fu)} \\
& C(c, Fj)
}$$

For each element $x \in X$, the family $\tau_j(x) : c \rightarrow Fj$ forms a cone from $c$ to $F$ in $C$. Since $v : b \rightarrow F$ is a limiting cone, there exists a unique arrow $h_x : c \rightarrow b$ with $v_j \circ h_x = \tau_j(x)$ for all $j$. Define $\theta : X \rightarrow C(c, b)$ by $\theta(x) = h_x$. Then $C(c, v_j) \circ \theta = \tau_j$, and $\theta$ is unique with this property. Hence $C(c, v)$ is a limiting cone, so $C(c, -)$ preserves limits.

The same proof works with $\mathbf{Set}$ replaced by any category $\mathbf{Ens}$ of sets. The formulation using the adjunction $\operatorname{Cone}(X, C(c, F-)) \cong \mathbf{Set}(X, \operatorname{Cone}(c, F)) \cong \mathbf{Set}(X, C(c, \operatorname{Lim} F))$ yields the identities

$$\operatorname{Lim} C(c, F-) \cong C(c, \operatorname{Lim} F), \qquad \prod_i C(c, a_i) \cong C(c, \prod_i a_i).$$

The contravariant case follows by noting $C(-, c) = C^{\text{op}}(c, -)$, so it carries colimits in $C$ (which are limits in $C^{\text{op}}$) to limits in $\mathbf{Set}$. $\square$
