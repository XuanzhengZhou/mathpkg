---
role: proof
locale: en
of_concept: structure-constants-identities
source_book: gtm009
source_chapter: "1"
source_section: "1.4"
---

The identities are obtained by expanding the defining axioms in terms of the basis $\{x_i\}$.

From (L2), $[x_i, x_i] = 0$, we have $\sum_k a_{ii}^k x_k = 0$, so $a_{ii}^k = 0$ for all $i, k$ by linear independence.

From anticommutativity (L2'), $[x_i, x_j] = -[x_j, x_i]$, we obtain:
$$\sum_k a_{ij}^k x_k = -\sum_k a_{ji}^k x_k,$$
so $a_{ij}^k = -a_{ji}^k$, or equivalently $a_{ij}^k + a_{ji}^k = 0$.

For the Jacobi identity (L3), compute $[x_i[x_j, x_\ell]]$:
$$[x_i, \sum_k a_{j\ell}^k x_k] = \sum_k a_{j\ell}^k [x_i, x_k] = \sum_k \sum_m a_{j\ell}^k a_{ik}^m x_m.$$

The full Jacobi identity $[x_i[x_j x_\ell]] + [x_j[x_\ell x_i]] + [x_\ell[x_i x_j]] = 0$ becomes:
$$\sum_m \left(\sum_k a_{ij}^k a_{k\ell}^m\right) x_m + \sum_m \left(\sum_k a_{j\ell}^k a_{ki}^m\right) x_m + \sum_m \left(\sum_k a_{\ell i}^k a_{kj}^m\right) x_m = 0.$$

By linear independence of $\{x_m\}$, for each $m$:
$$\sum_k (a_{ij}^k a_{k\ell}^m + a_{j\ell}^k a_{ki}^m + a_{\ell i}^k a_{kj}^m) = 0.$$

(Note: the first term in the textbook uses $a_{ij}^k a_{k\ell}^m$ where the indices match the cyclic pattern $i \to j \to \ell \to i$.)
