---
role: proof
locale: en
of_concept: affine-isomorphism-characterization
source_book: gtm049
source_chapter: "3"
source_section: "3.5"
---

Let $\alpha: \mathcal{A}(a+M) \to \mathcal{A}(a'+M')$ be an affine isomorphism. We first assume $0_V\alpha = 0_{V'}$ and write $v\alpha = v'$ for all $v \in V$.

When $\dim V \geq 2$, choose a non-zero vector $a$ in $V$. Since $\alpha$ is an isomorphism taking the line $[a]$ to $[a']$, for each $x \in F$ there is a unique $x' \in F'$ such that $(xa)' = x'a'$. One shows that this mapping $x \mapsto x'$ is independent of the choice of $a$: if $a$ and $b$ are linearly independent, then parallelism considerations force the scalars to agree. If $a$ and $b$ are linearly dependent, choose a third vector $c$ not on $[a]$ and use transitivity.

Thus there is a unique mapping $\zeta: x \mapsto x'$ of $F$ onto $F'$ such that $(xa)' = x'a'$ for all $x \in F$ and all $a \in V$.

If $a$ and $b$ are linearly independent, $\alpha$ carries the parallelogram $a, 0_V, b, a+b$ into $a', 0_{V'}, b', a'+b'$, giving $(a+b)' = a'+b'$. This extends to all $a, b$ using a third vector $c$ when $a, b$ are dependent.

From these rules one deduces that $\zeta$ satisfies $(x+y)' = x'+y'$ and $(xy)' = x'y'$ for all $x, y \in F$, so $\zeta$ is a field isomorphism.

The mapping $g: M \to M'$ defined by $g(v) = \alpha(v) - a'$ (after translating the affine isomorphism appropriately) is then a semi-linear isomorphism with respect to $\zeta$. The uniqueness of $g$ follows as in the affinity case (p. 43), and $\zeta$ is uniquely determined by $g$.

When $\dim V = 1$, the same construction gives only a bijection $\zeta$ of $F$ onto $F'$, but the field isomorphism properties cannot be established without additional structure.
