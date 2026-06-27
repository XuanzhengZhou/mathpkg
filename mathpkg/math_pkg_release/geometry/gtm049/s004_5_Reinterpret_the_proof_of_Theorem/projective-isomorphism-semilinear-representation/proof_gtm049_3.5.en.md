---
role: proof
locale: en
of_concept: projective-isomorphism-semilinear-representation
source_book: gtm049
source_chapter: "3"
source_section: "3.5"
---

Let $\pi: \mathcal{P}(V) \to \mathcal{P}(V')$ be an isomorphism. Choose a hyperplane $H$ in $\mathcal{P}(V)$ and let $H' = H\pi$. Then $H'$ is a hyperplane in $\mathcal{P}(V')$. Let $A$ and $A'$ be the affine geometries determined by $H$ and $H'$ respectively.

By Proposition 3, $\pi$ restricts to an affine isomorphism $\alpha: A \to A'$. Now apply Theorem 5 to $\alpha$:

If $\operatorname{pdim} \mathcal{P} = 1$, then $\dim A = 1$, so Theorem 5 gives a one--one mapping of $F$ onto $F'$.

If $\operatorname{pdim} \mathcal{P} \geq 2$, then $\dim A \geq 2$, so Theorem 5 gives an isomorphism $\zeta$ of $F$ onto $F'$ and a semi-linear isomorphism $g$ of the direction space $M$ of $A$ onto the direction space $M'$ of $A'$ with respect to $\zeta$.

Now $M$ is a hyperplane in $V$ and $M'$ is a hyperplane in $V'$. Choose vectors $c \in V \setminus M$ and $c' \in V' \setminus M'$ such that the affine isomorphism $\alpha$ corresponds to the restriction of $\mathcal{A}(g)$ after suitable translation. Extend $g$ to $f: V \to V'$ by setting $cf = c'$ and defining $f$ on all of $V = Fc \oplus M$ by $(xc + m)f = (x\zeta)c' + mg$. Then $f$ is a semi-linear isomorphism of $V$ onto $V'$ with respect to $\zeta$, and $\mathcal{P}(f) = \pi$.

The projective isomorphism $\mathcal{P}(f)$ induces the given affine isomorphism $\beta$ on $A$. But $\pi$ also induces $\beta$. Hence $\mathcal{P}(f) = \pi$ by the uniqueness part of Proposition 3.
