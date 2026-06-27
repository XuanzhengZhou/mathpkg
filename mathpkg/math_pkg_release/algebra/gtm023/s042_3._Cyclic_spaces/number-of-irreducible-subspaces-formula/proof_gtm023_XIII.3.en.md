---
role: proof
locale: en
of_concept: number-of-irreducible-subspaces-formula
source_book: gtm023
source_chapter: "XIII"
source_section: "3"
---

Consider the transformation $\psi = f(\varphi)$. Since the subspaces $F_\kappa$ (direct sum of irreducible subspaces of dimension $p\kappa$) are stable under $\psi$, we have $\psi E = \sum \psi F_\kappa$. The dimension of each irreducible subspace $E_\kappa^\lambda$ decreases by $p$ under $\psi$, so $\dim \psi F_\kappa = p(\kappa-1)N_\kappa$. Hence
$$r(\psi) = p \sum_{\kappa=2}^{k} (\kappa-1)N_\kappa.$$

Repeating for higher powers:
$$r(\psi^j) = p \sum_{\kappa=j+1}^{k} (\kappa-j)N_\kappa \quad j=1,\ldots,k.$$

Taking differences yields
$$N_j = \frac{1}{p} \left[ r(\psi^{j+1}) + r(\psi^{j-1}) - 2r(\psi^j) \right] \quad j = 1, \ldots, k.$$
