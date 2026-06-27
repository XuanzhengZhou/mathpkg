---
role: proof
locale: en
of_concept: kummers-theorem
source_book: gtm028
source_chapter: "V"
source_section: "§13. A theorem of Kummer"
---

Denote by $k$ the field $R/\mathfrak{p}$. Consider the composite homomorphism:

$$R[X] \to k[X] \to k[X]/(f_i(X)),$$

where the first map is reduction modulo $\mathfrak{p}$, and the second is the canonical projection. The kernel is $(\mathfrak{p}R[X], F_i(X))$ and contains $F(X)$ since $F(y)=0$ implies $\bar{F}(X) = \prod_i f_i(X)^{e_i}$ has $f_i(X)$ as a factor.

By passage to residue class rings, we obtain a homomorphism:

$$h_i : R' = R[y] = R[X]/(F(X)) \to k[X]/(f_i(X)).$$

Since $f_i(X)$ is irreducible over $k$, the ring $k[X]/(f_i(X))$ is a field. The kernel $\mathfrak{P}_i = \ker(h_i)$ is therefore a maximal ideal of $R'$. As $\mathfrak{P}_i$ contains $\mathfrak{p}$, and $\mathfrak{p}$ is prime, $\mathfrak{P}_i \cap R = \mathfrak{p}$. The ideals $\mathfrak{P}_i$ are distinct because the polynomials $f_i(X)$ are distinct.

The kernel is $\mathfrak{P}_i = R'\mathfrak{p} + F_i(y)R'$ where $F_i(X) \in R[X]$ is any lift of $f_i(X)$.

When the coefficients of $\prod_i (F_i(X))^{e_i}$ are reduced modulo $\mathfrak{p}$, the result is $\bar{F}(X)$. Since $F(y)=0$, the product $\prod_i (F_i(y))^{e_i} \in R'\mathfrak{p}$. Hence $\prod_i \mathfrak{P}_i^{e_i} \subset R'\mathfrak{p}$.

The containment $\mathfrak{P}_i \supset R'\mathfrak{p}$ is clear. By the Chinese Remainder Theorem and degree considerations ($\sum_i e_i \deg(f_i) = n = [K':K]$), we obtain equality $\mathfrak{p}R' = \prod_i \mathfrak{P}_i^{e_i}$.

Each $e_i$ is the reduced ramification index of $\mathfrak{P}_i$, and $\deg(f_i) = [k[X]/(f_i(X)) : k] = [R'/\mathfrak{P}_i : R/\mathfrak{p}]$ is the residue field degree.
