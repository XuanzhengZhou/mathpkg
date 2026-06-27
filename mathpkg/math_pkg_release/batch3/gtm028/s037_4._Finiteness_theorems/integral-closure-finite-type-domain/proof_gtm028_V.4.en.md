---
role: proof
locale: en
of_concept: integral-closure-finite-type-domain
source_book: gtm028
source_chapter: "V"
source_section: "§4. Finiteness theorems"
---

We first achieve a reduction to the case in which $F$ is the quotient field of $A$. For this purpose we observe that there exists a basis $\{y_1, \cdots, y_q\}$ of $F$ over $k(x_1, \cdots, x_n)$ composed of elements which are integral over $A$ (see the argument from the proof of Theorem 7). Then the ring $A^0 = A[y_1, \cdots, y_q]$ is a finite integral domain over $k$, is integral over $A$, and admits $F$ as its quotient field. This achieves the desired reduction since $A'$ is obviously the integral closure of $A^0$.

We now prove Theorem 9 under the additional hypotheses that $k$ is infinite and that $F = k(x_1, \cdots, x_n)$ is separably generated over $k$. Under these assumptions there exist, by Theorem 8, $d$ linear combinations $z_1, \cdots, z_d$ of the $x_i$ such that the subring $B = k[z_1, \cdots, z_d]$ of $A$ is a polynomial ring, over which $A$ is integral and separable. Owing to the transitivity of integral dependence (§1, Theorem 2), $A'$ is the integral closure of $B$ in $F$. Since $B$ is integrally closed (as a polynomial ring over a field) and Noetherian, Corollary 1 to Theorem 7 shows that $A'$ is a finite $B$-module. It is, *a fortiori*, a finite $A$-module, and a finite integral domain over $k$.

In the general case, we consider $k(x_1, \cdots, x_n)$ as a subfield of its algebraic closure, which contains the algebraic closure $\overline{k}$ of $k$. Since $\overline{k}$ is infinite and since $k(x_1, \cdots, x_n) \otimes_k \overline{k}$ is separably generated over $\overline{k}$ (or by passing to a purely inseparable extension and using the separable case), the theorem follows by descent.
