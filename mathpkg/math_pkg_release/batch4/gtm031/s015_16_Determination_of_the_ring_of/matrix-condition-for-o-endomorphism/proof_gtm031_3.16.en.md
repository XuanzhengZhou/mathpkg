---
role: proof
locale: en
of_concept: matrix-condition-for-o-endomorphism
source_book: gtm031
source_chapter: "3"
source_section: "16"
---

Write each image as $g_i = f_i B = \sum_{j=1}^{t} \beta_{ij} f_j$ for some $\beta_{ij} \in \mathfrak{o}$. Note that the $\beta_{ij}$ in column $j$ are only determined modulo $\delta_j$, since $f_j$ has order ideal $(\delta_j)$, and adding a multiple of $\delta_j$ to $\beta_{ij}$ changes $g_i$ by a multiple of $\delta_j f_j = 0$.

The condition $\delta_i g_i = 0$ becomes

$$\delta_i \sum_{j=1}^{t} \beta_{ij} f_j = \sum_{j=1}^{t} (\delta_i \beta_{ij}) f_j = 0.$$

Since $\mathfrak{R}$ is a direct sum of the cyclic modules $\{f_j\}$, this equality holds if and only if each component vanishes in $\{f_j\}$, which means $\delta_i \beta_{ij} f_j = 0$ in $\{f_j\}$. This is equivalent to $\delta_j \mid \delta_i \beta_{ij}$, i.e.,

$$\delta_i \beta_{ij} \equiv 0 \pmod{\delta_j}.$$

Thus there exist $\gamma_{ij} \in \mathfrak{o}$ such that $\delta_i \beta_{ij} = \gamma_{ij} \delta_j$, which in matrix form is precisely $\operatorname{diag}(\delta_1, \ldots, \delta_t) (\beta) = (\gamma) \operatorname{diag}(\delta_1, \ldots, \delta_t)$.
