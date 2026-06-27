---
role: proof
locale: en
of_concept: valence-formula-modular-function
source_book: gtm007
source_chapter: "VII"
source_section: "1"
---

**Finiteness.** Since $\tilde{f}$ is meromorphic, there exists $r > 0$ such that $\tilde{f}$ has no zero nor pole for $0 < |q| < r$; this means $f$ has no zero nor pole for $\operatorname{Im}(z) > \frac{1}{2\pi} \log \frac{1}{r}$. The compactness of $D \cap \{z \mid \operatorname{Im}(z) \leq T\}$ for any $T$ implies $f$ has only finitely many zeros and poles modulo $G$.

**Integration over the contour.** Integrate $\frac{1}{2\pi i} \frac{df}{f}$ over the boundary of the truncated fundamental domain. The contour is a polygon with vertices on the boundary of $D$, modified near $i, \rho, -\bar{\rho}$ by small arcs. As the truncation height $T \to \infty$, the top horizontal segment contributes $-v_\infty(f)$ to the total integral (by the argument principle applied to $\tilde{f}$ at $q = 0$).

For the arcs near $\rho$ (radius $\to 0$), the angle is $\pi/3$, so the contribution is $-\frac{1}{6} v_\rho(f)$. For the arc near $i$ (angle $\pi$), the contribution is $-\frac{1}{2} v_i(f)$. For the other arc near $\rho$, another $-\frac{1}{6} v_\rho(f)$. Vertices on the boundary not at $i, \rho, -\bar{\rho}$ contribute $-\frac{1}{2} v_p(f)$ each (since the contour makes a $\pi$ turn at such points).

Now use the $G$-invariance properties:
- $T$ transforms the arc $AB$ into $ED'$; since $f(Tz) = f(z)$, the integrals along $AB$ and $D'E$ cancel.
- $S$ transforms the arc $B'C$ onto $DC'$; using $f(Sz) = z^{2k} f(z)$, we get
$$\frac{df(Sz)}{f(Sz)} = 2k \frac{dz}{z} + \frac{df(z)}{f(z)},$$
so the combined contribution of $B'C$ and $C'D$ is $\frac{1}{2\pi i} \int_{B'}^C (-2k \frac{dz}{z}) \to -2k(-\frac{1}{12}) = \frac{k}{6}$ as the radii tend to $0$.

Equating the two expressions for the total integral gives the valence formula. If $f$ has zeros or poles on the boundary of $D$, the contour is modified by small detours around them, and the same reasoning applies by passing to the limit.
