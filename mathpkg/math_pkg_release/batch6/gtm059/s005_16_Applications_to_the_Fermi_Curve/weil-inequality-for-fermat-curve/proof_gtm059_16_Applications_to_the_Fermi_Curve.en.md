---
role: proof
locale: en
of_concept: weil-inequality-for-fermat-curve
source_book: gtm059
source_chapter: "16"
source_section: "Applications to the Fermat Curve"
---

**Note:** The source text for this section is severely degraded by OCR. The following proof sketch reconstructs the main argument from Lang's Cyclotomic Fields, Chapter 16.

The Fermat curve $V: X^n + Y^n = Z^n$ over $\mathbf{F}_q$ (with $q = p^f$, $p \nmid n$) can be studied via the covering map to $\mathbf{P}^1$ given by $(X:Y:Z) \mapsto (X^n : Z^n)$. The zeta function $Z(V,T)$ is expressed using Jacobi sums. Specifically, for each pair of multiplicative characters $\chi_1, \chi_2$ of $\mathbf{F}_q^\times$ with $\chi_1^n = \chi_2^n = \varepsilon$ (the trivial character), the Jacobi sum

$$J(\chi_1, \chi_2) = \sum_{t \in \mathbf{F}_q} \chi_1(t) \chi_2(1-t)$$

contributes to the point count. The Weil inequality for the Fermat curve follows from the fact that each such Jacobi sum has absolute value $\sqrt{q}$, which is a consequence of the Hasse-Davenport relation and the fact that Gauss sums $g(\chi)$ satisfy $|g(\chi)| = \sqrt{q}$ for nontrivial characters.

The factorization $Z(V,T) = \prod_\chi L(T,\chi)$ with each $L(T,\chi) = 1 - a_\chi T$ and $|a_\chi| = \sqrt{q}$ then yields the Weil bound
$$|N_\nu - (q^\nu + 1)| \leq 2g q^{\nu/2}$$
where $g = \frac{(n-1)(n-2)}{2}$ is the genus of the Fermat curve.
