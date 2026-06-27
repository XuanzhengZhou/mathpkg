---
role: proof
locale: en
of_concept: parallel-vector-field-characterization
source_book: gtm048
source_chapter: "7"
source_section: "7.6"
---

Suppose $X = aY$ for some $a \in \mathbb{R}$. Then for all $(z, Z) \in TM$,
$$D_Z X = a\left\{Z[\omega^i(Y)] + \omega_j^i(Z) \omega^j(Y)\right\} X_i = a \omega_3^i(Z) X_i = 0,$$
where we have used Section 3.6.1e and the proof of Proposition 7.6.1 which shows that the only non-zero connection forms involve $\omega^3$ and $\omega^4$, and that $Y$ is a linear combination of $X_3$ and $X_4$ with the property that its covariant derivative vanishes.

Conversely, suppose $DX = 0$. Then $\hat{R}(\cdot, X, \cdot, \cdot) = 0$ by the definition of a curvature tensor. Computing $\hat{R}(Z, X, W, V)$ using the non-zero curvature components $R_{1414}$ and $R_{1424}$ from Proposition 7.6.1, one finds that the components of $X$ in the $X_1$ and $X_2$ directions must vanish. Moreover, the $X_4$ component must also vanish, leaving only the $X_3$ component. Since $Y$ spans the parallel vector fields in the $\{X_3, X_4\}$ plane, we must have $X = aY$ for some constant $a \in \mathbb{R}$.
