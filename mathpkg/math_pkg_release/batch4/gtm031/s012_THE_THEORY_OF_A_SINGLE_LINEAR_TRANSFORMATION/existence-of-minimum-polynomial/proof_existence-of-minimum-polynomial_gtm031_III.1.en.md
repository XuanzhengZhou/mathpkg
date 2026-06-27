---
role: proof
locale: en
of_concept: existence-of-minimum-polynomial
source_book: gtm031
source_chapter: "III"
source_section: "1"
---

From the linear dependence relation, we have
$$A^m - \mu_{m-1} A^{m-1} - \mu_{m-2} A^{m-2} - \cdots - \mu_0 1 = 0.$$
Hence the polynomial
$$\mu(\lambda) = \lambda^m - \mu_{m-1} \lambda^{m-1} - \mu_{m-2} \lambda^{m-2} - \cdots - \mu_0$$
which is nonzero is in the kernel $\mathfrak{K}$ of the polynomial evaluation homomorphism. This shows that $\mathfrak{K} \neq (0)$.

Now $\mathfrak{K}$ is an ideal in the principal ideal domain $\Phi[\lambda]$, so $\mathfrak{K} = (\nu(\lambda))$ for some monic polynomial $\nu(\lambda)$. Since $\mu(\lambda) \in \mathfrak{K}$, we have $\nu(\lambda) \mid \mu(\lambda)$.

On the other hand, if $\nu(\lambda)$ had degree less than $m$, then $\nu(A) = 0$ would give a linear dependence among $1, A, \dots, A^{\deg \nu}$ contradicting the minimality of $m$. Thus $\deg \nu \ge m = \deg \mu$, which together with $\nu \mid \mu$ implies $\nu(\lambda) = \mu(\lambda)$ up to a constant factor. Since both are monic, $\nu(\lambda) = \mu(\lambda)$. Therefore $\mu(\lambda)$ generates $\mathfrak{K}$ and is the minimum polynomial of $A$.
