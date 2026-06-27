---
role: proof
locale: en
of_concept: tower-theorem-finite-extensions
source_book: gtm028
source_chapter: "II"
source_section: "3. Algebraic extensions"
---

Let $\{\omega_1, \ldots, \omega_n\}$ be a basis of $K$ over $k$ and $\{\xi_1, \ldots, \xi_m\}$ a basis of $L$ over $K$.

**Spanning.** Every element $\alpha \in L$ can be expressed as
$$\alpha = \sum_{j=1}^{m} a_j \xi_j, \qquad a_j \in K.$$
Each $a_j \in K$ can in turn be expressed as
$$a_j = \sum_{i=1}^{n} c_{ij} \omega_i, \qquad c_{ij} \in k.$$
Substituting,
$$\alpha = \sum_{j=1}^{m} \left( \sum_{i=1}^{n} c_{ij} \omega_i \right) \xi_j = \sum_{i=1}^{n} \sum_{j=1}^{m} c_{ij} \omega_i \xi_j.$$
Thus the $mn$ elements $\omega_i \xi_j$ span $L$ over $k$.

**Linear independence.** Suppose
$$\sum_{i=1}^{n} \sum_{j=1}^{m} c_{ij} \omega_i \xi_j = 0, \qquad c_{ij} \in k.$$
Set $C_j = \sum_{i=1}^{n} c_{ij} \omega_i$. Then $C_j \in K$ and
$$\sum_{j=1}^{m} C_j \xi_j = 0.$$
Since the $\xi_j$ form a basis of $L$ over $K$, we must have $C_j = 0$ for all $j = 1, 2, \ldots, m$. From $C_j = \sum_{i=1}^{n} c_{ij} \omega_i = 0$ and the linear independence of the $\omega_i$ over $k$, we conclude that all $c_{ij} = 0$.

Therefore the $mn$ elements $\omega_i \xi_j$ form a basis of $L$ over $k$.
