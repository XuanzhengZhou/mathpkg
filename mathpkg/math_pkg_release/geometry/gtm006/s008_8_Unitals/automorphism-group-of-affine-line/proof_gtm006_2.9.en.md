---
role: proof
locale: en
of_concept: automorphism-group-of-affine-line
source_book: gtm006
source_chapter: "2"
source_section: "9"
---

*Proof.* The affine line $\mathcal{A}$ is obtained from the projective line $\mathcal{P}(V)$ (where $\dim V = 2$) by discarding the point $\infty$. In parametric coordinates, the discarded point corresponds to $\infty$, and the remaining points are identified with elements of $K$. The automorphism group $\text{Aut}\,\mathcal{A}$ is the subgroup of $\text{P}\Gamma\text{L}(V)$ fixing $\infty$.

A general element of $\text{P}\Gamma\text{L}(V)$ acting on the projective line has the form $x \mapsto (a x^{\alpha} + b)/(c x^{\alpha} + d)$ with $ad - bc \neq 0$. The condition that $\infty$ is fixed forces $c = 0$, giving $x \mapsto (a/d) x^{\alpha} + b/d$. Setting $k = a/d$ and renaming $b$ yields the stated form $x \mapsto k x^{\alpha} + b$.

The subgroups $\Lambda_1$ (fix $\alpha = 1$) and $\Lambda_2$ (fix $\alpha = 1, k = 1$) are clearly normal by direct computation, and the isomorphisms for the factor groups follow immediately from the definitions. $\square$
