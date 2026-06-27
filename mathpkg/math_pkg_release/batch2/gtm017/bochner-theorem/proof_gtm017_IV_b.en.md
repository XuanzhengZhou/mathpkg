---
role: proof
locale: en
of_concept: bochner-theorem
source_book: gtm017
source_chapter: "IV"
source_section: "b"
---
Necessity: For a characteristic function $\varphi(t) = \int e^{itx} dF(x)$, continuity follows from dominated convergence. Positive definiteness:
$$\sum_{i,j} c_i \bar{c}_j \varphi(t_i-t_j) = \int \left|\sum_i c_i e^{it_i x}\right|^2 dF(x) \geq 0.$$

Sufficiency (Bochner): The positive definite continuous function $\varphi$ with $\varphi(0)=1$ can be inverted via a limit procedure to yield a non-decreasing bounded function $F$, which after normalization gives a distribution function whose Fourier-Stieltjes transform is $\varphi$.
