---
role: proof
locale: en
of_concept: simple-module-classes-freely-generate-representation-ring
source_book: gtm020
source_chapter: "9"
source_section: "7"
---

**Proof.** Let $M$ and $N$ be simple $G$-modules. Using the Haar measure, define the inner product $\langle f, g \rangle = \int_G f(s) \overline{g(s)} \, d\mu(s)$ on $C_F(G)$. A computation using matrix elements of $s_M$ shows that $\langle \chi_M, \chi_N \rangle = 1$ if $M \cong N$ and $0$ otherwise (orthogonality of characters of simple modules).

If $\sum_i n_i [M_i] = 0$ in $R_F(G)$ with simple modules $M_i$, then taking characters gives $\sum_i n_i \chi_{M_i} = 0$. Taking the inner product with $\chi_{M_j}$ yields $n_j \langle \chi_{M_j}, \chi_{M_j} \rangle = n_j = 0$. Hence the simple module classes are linearly independent over $\mathbf{Z}$.

Combined with the generation result (Corollary 6.6), they freely generate $R_F(G)$ as an abelian group. $\square$
