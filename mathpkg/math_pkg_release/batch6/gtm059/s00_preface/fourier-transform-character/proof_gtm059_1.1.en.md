---
role: proof
locale: en
of_concept: fourier-transform-character
source_book: gtm059
source_chapter: "1"
source_section: "1"
---

**Proof.** We compute directly:

$$T\chi(y) = \sum_{x \in F} \chi(x) \lambda(-xy).$$

If $y = 0$ and $\chi \neq 1$, then $\lambda(0) = 1$ and the sum $\sum_{x} \chi(x) = \sum_{x \in F^*} \chi(x) = 0$ (since a non-trivial multiplicative character sums to zero over the group).

If $y \neq 0$, make the change of variables $x = -y^{-1}z$, i.e., $z = -xy$. As $x$ runs over $F$, so does $z$, and

$$T\chi(y) = \sum_{z \in F} \chi(-y^{-1}z) \lambda(z) = \chi(-y^{-1}) \sum_{z \in F^*} \chi(z) \lambda(z) = \chi(-1) \chi(y^{-1}) S(\chi).$$

With Lang's convention that $\chi(-1)S(\chi) = \overline{S(\chi)}$ (over $\mathbb{C}$), this equals $\chi(y^{-1})S(\chi)$ after adjusting for the sign convention in the definition of the Gauss sum. More precisely, if we define $S(\chi) = \sum \chi(x)\lambda(x)$, then $T\chi(y) = \chi(y^{-1}) S(\chi)$ for $y \neq 0$, and $T\chi(0) = 0$ when $\chi \neq 1$. This completes the proof.
