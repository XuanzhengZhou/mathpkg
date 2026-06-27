---
role: proof
locale: en
of_concept: analytic-class-number-formula
source_book: gtm059
source_chapter: "3"
source_section: "Complex Analytic Class Number Formulas"
---

The proof proceeds by comparing the residue at $s = 1$ of the Dedekind zeta function $\zeta_K(s)$ with the product of Dirichlet $L$-functions. For an abelian extension $K/\mathbb{Q}$ with Galois group $G$, the zeta function factorizes as:

$$\zeta_K(s) = \prod_{\chi \in \widehat{G}} L(s, \chi)$$

where $\widehat{G}$ is the character group of $G$, and $L(s, \chi_0) = \zeta(s)$ for the trivial character $\chi_0$.

The Dedekind zeta function has a simple pole at $s = 1$ with residue:

$$\operatorname{Res}_{s=1} \zeta_K(s) = \frac{2^{r_1} (2\pi)^{r_2} h R}{w \sqrt{|d|}}$$

On the other hand, $\zeta(s)$ has a simple pole at $s = 1$ with residue $1$, while each $L(s, \chi)$ for $\chi \neq 1$ is holomorphic at $s = 1$. Therefore:

$$\operatorname{Res}_{s=1} \zeta_K(s) = \left( \operatorname{Res}_{s=1} \zeta(s) \right) \cdot \prod_{\chi \neq 1} L(1, \chi) = \prod_{\chi \neq 1} L(1, \chi)$$

Equating the two expressions for the residue yields the analytic class number formula. The proof involves the functional equation of the Dedekind zeta function, the Kronecker limit formula, and the factorization of $\zeta_K(s)$ into $L$-series corresponding to the characters of the abelian Galois group. Chapter XII of Lang's *Algebraic Number Theory* provides the full details of the analytic continuation and functional equations needed.

The decomposition of the $L$-series product uses the multiplicative form of $L(s, \chi)$ and the fact that for each prime $p$ not dividing the conductor $m$, the Euler factor $(1 - \chi(p) p^{-s})^{-1}$ decomposes according to the factorization of $p$ in $K$. The identity reduces to showing that for each prime $p$, the product over characters of the local factors matches the local zeta factor. For $p \mid m$, the ramified primes require special treatment using the conductor.
