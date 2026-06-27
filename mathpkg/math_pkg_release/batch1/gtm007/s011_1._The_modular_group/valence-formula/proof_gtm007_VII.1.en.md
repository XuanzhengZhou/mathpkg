---
role: proof
locale: en
of_concept: valence-formula
source_book: gtm007
source_chapter: "VII"
source_section: "§1. The modular group"
---

The proof uses contour integration of $f'/f$ around the boundary of the fundamental domain $\mathcal{F}$. By the argument principle,
$$
\frac{1}{2\pi i} \oint_{\partial \mathcal{F}} \frac{f'(z)}{f(z)} dz = \sum_{p \in \operatorname{int}(\mathcal{F})} v_p(f).
$$
The contour integral decomposes into segments along the boundary. The contributions from the vertical lines cancel (due to $f(z+1) = f(z)$), the arc from $\rho$ to $i$ is mapped by $S$ to another arc, and the remaining integral gives $k/12$. The $v_\infty$ term arises from the horizontal segment.
