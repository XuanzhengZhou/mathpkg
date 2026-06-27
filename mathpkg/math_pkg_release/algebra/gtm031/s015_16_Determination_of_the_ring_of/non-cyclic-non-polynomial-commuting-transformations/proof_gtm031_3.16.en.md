---
role: proof
locale: en
of_concept: non-cyclic-non-polynomial-commuting-transformations
source_book: gtm031
source_chapter: "3"
source_section: "16"
---

From the vector space dimension computation, we have $\dim_\Phi \mathfrak{B} = N = \sum_{j=1}^{t} (2t - 2j + 1) n_j$ where $n_j = \deg \delta_j$.

If $t > 1$, then $N > \sum_{j=1}^{t} n_j = n$. Meanwhile, $\dim_\Phi \mathfrak{A} = \dim_\Phi \Phi[A] = n_t$ (the degree of the minimal polynomial of $A$, which is the last invariant factor $\delta_t$). Since $\mathfrak{A} \subseteq \mathfrak{B}$ and $\dim \mathfrak{A} = n_t$ while $\dim \mathfrak{B} = N > n_t$ (for $t > 1$), we have $\mathfrak{B} \supsetneq \mathfrak{A}$. Thus there exist elements in $\mathfrak{B}$ that are not in $\mathfrak{A}$, i.e., linear transformations commuting with $A$ that are not polynomials in $A$.

The condition $t = 1$ is precisely the condition that $A$ is cyclic (the vector space is a cyclic module over $\Phi[A]$), hence the statement is the converse of the corollary to Theorem 17.
