---
role: proof
locale: en
of_concept: matrix-of-transformation-ae
source_book: gtm031
source_chapter: "IV"
source_section: "2"
---

We compute $\bar{f}_k A_E$ for $k = r+1, \ldots, n$. By definition of $A_E$,

$$\bar{f}_k A_E = f_k (AE - EA) = f_k AE - f_k EA.$$

Since $E$ is the projection onto $\mathfrak{S} = [f_1, \ldots, f_r]$ and vanishes on the complement $U = [f_{r+1}, \ldots, f_n]$, we have $f_k E = 0$ for $k > r$. Therefore

$$\bar{f}_k A_E = f_k AE.$$

Now $f_k A = \sum_{j=1}^{n} \beta_{kj} f_j$. By the reduced form, the coefficients for $j = r+1, \ldots, n$ in the first $r$ rows are zero, but for $k > r$ they may be non-zero. Applying $E$ projects onto the first $r$ coordinates:

$$f_k A E = \sum_{j=1}^{r} \beta_{kj} f_j.$$

Thus

$$\bar{f}_k A_E = \sum_{j=1}^{r} \beta_{kj} f_j, \quad k = r+1, \ldots, n.$$

This shows that the matrix of $A_E$ relative to the bases $(\bar{f}_{r+1}, \ldots, \bar{f}_n)$ for $\bar{\Re}$ and $(f_1, \ldots, f_r)$ for $\mathfrak{S}$ is precisely the $(n-r) \times r$ lower-left block $A_{21}$ appearing in the reduced form of the matrix of $A$.
