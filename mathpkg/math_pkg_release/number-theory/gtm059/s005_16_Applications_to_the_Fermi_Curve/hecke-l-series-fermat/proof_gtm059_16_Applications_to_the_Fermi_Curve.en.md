---
role: proof
locale: en
of_concept: hecke-l-series-fermat
source_book: gtm059
source_chapter: "16"
source_section: "Applications to the Fermat Curve"
---

**Note:** The source text for this section is severely degraded by OCR. The following proof sketch reconstructs the argument from Lang's Cyclotomic Fields.

The point count $N_\nu$ on the Fermat curve $X^n + Y^n = Z^n$ over $\mathbf{F}_{q^\nu}$ can be expressed using multiplicative characters. For each nontrivial character $\chi$ of order dividing $n$ on $\mathbf{F}_{q^\nu}^\times$, the Jacobi sum

$$J_\nu(\chi^a, \chi^b) = \sum_{t \in \mathbf{F}_{q^\nu}} \chi^a(t) \chi^b(1-t)$$

appears in the counting. Specifically, the number of solutions to $X^n + Y^n = Z^n$ in projective space is

$$N_\nu = q^\nu + 1 + \sum_{\substack{a,b=0\\ a+b \not\equiv 0 \pmod{n}}}^{n-1} J_\nu(\chi^a, \chi^b).$$

Using the Hasse-Davenport relation, each Jacobi sum $J_\nu(\chi^a, \chi^b)$ is related to a Gauss sum, which in turn corresponds to the value of a Hecke character at the prime above $p$. Summing over $\nu$ and taking the logarithmic derivative yields the factorization of $Z(V,T)$ as a product of $L$-series

$$L(T, \chi) = \exp\left(\sum_{\nu=1}^\infty \chi(\mathfrak{p}^\nu) \frac{T^\nu}{\nu}\right) = 1 - \chi(\mathfrak{p}) T$$

where $\mathfrak{p}$ is the prime ideal above $p$ in the appropriate cyclotomic field.
