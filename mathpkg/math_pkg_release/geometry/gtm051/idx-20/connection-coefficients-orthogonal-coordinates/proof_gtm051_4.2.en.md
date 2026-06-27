---
role: proof
locale: en
of_concept: connection-coefficients-orthogonal-coordinates
source_book: gtm051
source_chapter: "4"
source_section: "4.2"
---

In orthogonal coordinates we have $g_{12} = g_{21} = 0$, and the metric matrix is diagonal. Its inverse is also diagonal with $g^{11} = 1/g_{11}$, $g^{22} = 1/g_{22}$, and $g^{12} = g^{21} = 0$.

The Christoffel symbols are given by

$$\Gamma_{ij}^k = \frac{1}{2} \sum_{l} g^{kl}(g_{il,j} + g_{jl,i} - g_{ij,l}).$$

Since $g^{kl} = 0$ for $k \neq l$ in orthogonal coordinates, the sum reduces to the single term $l = k$:

$$\Gamma_{ij}^k = \frac{1}{2} g^{kk}(g_{ik,j} + g_{jk,i} - g_{ij,k}).$$

For $\Gamma_{ik}^k$ (taking $j=k$ above), we obtain

$$\Gamma_{ik}^k = \frac{1}{2} g^{kk}(g_{ik,k} + g_{kk,i} - g_{ik,k}) = \frac{1}{2} g^{kk} g_{kk,i} = \frac{g_{kk,i}}{2g_{kk}} = (\log\sqrt{g_{kk}})_i.$$

For $i \neq k$, the metric components $g_{ik}$ vanish identically, hence their derivatives also vanish: $g_{ik,j} = 0$. This yields

$$\Gamma_{ij}^k = \frac{1}{2} g^{kk}(0 + 0 - g_{ij,k}) = -\frac{g_{ij,k}}{2g_{kk}}.$$

When $i = j$, this gives $\Gamma_{ii}^k = -g_{ii,k}/2g_{kk}$ for $i \neq k$. When $i \neq j$, the off-diagonal $g_{ij} = 0$ implies $g_{ij,k} = 0$, so $\Gamma_{ij}^k = 0$ for all three indices distinct.
