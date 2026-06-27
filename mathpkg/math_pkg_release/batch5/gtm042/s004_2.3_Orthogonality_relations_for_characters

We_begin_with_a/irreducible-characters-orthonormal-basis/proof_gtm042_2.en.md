---
role: proof
locale: en
of_concept: irreducible-characters-orthonormal-basis
source_book: gtm042
source_chapter: "2"
source_section: "2.5"
---

Theorem 3 already established that the irreducible characters $\chi_1, \ldots, \chi_h$ are orthonormal. It remains to prove that they span the space $H$ of all class functions.

Let $f$ be a class function orthogonal to all $\chi_i$, i.e., $(f|\chi_i^*) = 0$ for all $i$. For any irreducible representation $\rho_i$ of character $\chi_i$, Proposition 6 implies that the associated operator $(\rho_i)_f$ is a homothety of ratio
$$\lambda_i = \frac{g}{n_i}(f|\chi_i^*) = 0.$$
Thus $(\rho_i)_f = 0$ for all irreducible representations $\rho_i$.

By complete reducibility, it follows that $\rho_f = 0$ for every representation $\rho$ of $G$. In particular, take $\rho$ to be the regular representation with basis $(e_t)_{t \in G}$. Computing the image of the basis vector $e_1$ under $\rho_f$,
$$\rho_f(e_1) = \sum_{t \in G} f(t)\rho_t(e_1) = \sum_{t \in G} f(t)e_t.$$
Since $\rho_f = 0$, we have $\sum_{t \in G} f(t)e_t = 0$, and by linear independence of the $e_t$, we conclude $f(t) = 0$ for all $t \in G$. Hence $f = 0$.

Therefore the orthogonal complement of the span of $\{\chi_1, \ldots, \chi_h\}$ is $\{0\}$, which means the $\chi_i$ span $H$. Together with orthonormality, they form an orthonormal basis. $\square$
