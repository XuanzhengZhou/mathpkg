---
role: proof
locale: en
of_concept: rank-of-rk-g
source_book: gtm042
source_chapter: "12"
source_section: "12.4"
---

Let $f$ be a class function on $G$ with values in $K$ that is invariant under $\Gamma_K$, i.e., $\sigma_t(f) = f$ for all $t \in \Gamma_K$. Expand $f$ in the basis of ordinary irreducible characters:

$$f = \sum_{\chi} c_{\chi} \chi,$$

where $\chi$ runs over the set of irreducible characters of $G$. We have to show that the $c_{\chi}$ belong to $K$, which, according to Galois theory, is equivalent to showing that they are invariant under the $\sigma_t$, $t \in \Gamma_K$. But, if $\varphi$ and $\chi$ are two class functions on $G$, then we have

$$\langle \Psi^t \varphi, \Psi^t \chi \rangle = \langle \varphi, \chi \rangle,$$

as can be easily verified. Whence

$$c_{\chi} = \langle f, \chi \rangle = \langle \Psi^t f, \Psi^t \chi \rangle = \langle \sigma_t(f), \sigma_t(\chi) \rangle = \sigma_t(\langle f, \chi \rangle) = \sigma_t(c_{\chi}),$$

which shows $c_{\chi} \in K$. Thus the irreducible characters over the algebraic closure, restricted to $\Gamma_K$-invariant class functions, provide a $K$-basis, and the number of irreducible representations of $G$ over $K$ equals the dimension of this space, namely the number of $\Gamma_K$-classes of $G$.
