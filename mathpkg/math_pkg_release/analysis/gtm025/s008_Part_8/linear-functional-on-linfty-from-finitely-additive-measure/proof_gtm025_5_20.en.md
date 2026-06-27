---
role: proof
locale: en
of_concept: linear-functional-on-linfty-from-finitely-additive-measure
source_book: gtm025
source_chapter: "5"
source_section: "20"
---

For $g \in \mathfrak{L}_{\infty}$, choose a bounded $f \in \mathfrak{L}_{\infty}$ such that $\|f - g\|_{\infty} = 0$ and $\|f\|_u = \|g\|_{\infty}$. By (20.32), we have
$$|L_{\tau}(g)| = \left|\int_X g d\tau\right| = \left|\int_X f d\tau\right| \leq \int_X |f| d|\tau| \leq \|f\|_u \|\tau\| = \|g\|_{\infty} \|\tau\|.$$
Thus $L_{\tau} \in \mathfrak{L}_{\infty}^*$ and $\|L_{\tau}\| \leq \|\tau\|$.

Let $\varepsilon > 0$ be given and select a measurable dissection $\{A_1, \ldots, A_n\}$ of $X$ such that
$$\sum_{j=1}^{n} |\tau(A_j)| > \|\tau\| - \varepsilon.$$
For each $j$, let $\alpha_j = \operatorname{sgn}(\overline{\tau(A_j)})$ and set $g = \sum_{j=1}^{n} \alpha_j \xi_{A_j}$. Then $\|g\|_{\infty} \leq 1$ and
$$L_{\tau}(g) = \int_X g \, d\tau = \sum_{j=1}^{n} \alpha_j \tau(A_j) = \sum_{j=1}^{n} |\tau(A_j)| > \|\tau\| - \varepsilon.$$
Hence $\|L_{\tau}\| = \|\tau\|$. $\square$
