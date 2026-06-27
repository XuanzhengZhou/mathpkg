---
role: proof
locale: en
of_concept: duality-isomorphism-semilinear-transformations
source_book: gtm006
source_chapter: "I"
source_section: "4. Vector Spaces"
---

No explicit proof is given in this section. The standard proof proceeds as follows:

For a non-singular semi-linear transformation $\alpha$ represented by matrix $A$ with automorphism $\sigma$, the dual map $\alpha'$ is defined by the condition that the evaluation pairing is preserved up to $\sigma$: $(vw')^\sigma = v^\alpha (w')^{\alpha'}$ for all $v \in V$, $w' \in V'$. In coordinates, if $v = (x_1,\dots,x_n)$ and $w'$ is the column vector $(y_1,\dots,y_n)^T$, then $vw' = \sum x_i y_i$. The condition gives $\sum (x_i^\sigma) (A_{ij}) (w')^{\alpha'}_j = (\sum x_i y_i)^\sigma = \sum x_i^\sigma y_i^\sigma$. This forces $(w')^{\alpha'} = A^{-1} (y_1^\sigma,\dots,y_n^\sigma)^T$.

The map is involutive because applying the transpose-inverse construction twice recovers the original matrix. It respects the semi-linear structure with the same automorphism $\sigma$. The image of $GL(V)$ (where $\sigma = \mathrm{id}$) under $\alpha \mapsto \alpha'$ is $GL(V')$, since the dual of a non-singular linear transformation is non-singular and linear.
