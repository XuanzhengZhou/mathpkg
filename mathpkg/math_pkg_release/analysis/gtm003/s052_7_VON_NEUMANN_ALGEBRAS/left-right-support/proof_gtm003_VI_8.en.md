---
role: proof
locale: en
of_concept: left-right-support
source_book: gtm003
source_chapter: "VI"
source_section: "8"
---

Represent $W$ as a von Neumann algebra in $\mathcal{L}(H)$ (cf. 7.1, Corollary 3). Let $x \in W$ with polar decomposition $x = u|x|$, where $|x| = \sqrt{x^*x}$ and $u$ is the unique partial isometry satisfying $u^*u = s_r(x)$ (the orthogonal projection onto $(\ker x)^\perp = \overline{\operatorname{ran}(x^*)}$) and $uu^* = s_l(x)$ (the orthogonal projection onto $\overline{\operatorname{ran}(x)}$).

Since $W$ is a von Neumann algebra, both $|x|$ and the spectral projections of $|x|$ belong to $W$, hence $u \in W$ as well. Then $uu^* = s_l(x)$ and $u^*u = s_r(x)$ are projections in $W$.

To see that $s_l(x)$ is the smallest projection $p \in W$ with $px = x$: if $px = x$, then $pu|x| = u|x|$, and since $u^*u$ is the projection onto the closure of the range of $|x|$, we have $pu = u$, so $puu^* = uu^*$, i.e., $p \geq s_l(x)$. The proof for $s_r(x)$ is symmetric. Finally, $s_l(x) = uu^* \sim u^*u = s_r(x)$ by definition of equivalence.
