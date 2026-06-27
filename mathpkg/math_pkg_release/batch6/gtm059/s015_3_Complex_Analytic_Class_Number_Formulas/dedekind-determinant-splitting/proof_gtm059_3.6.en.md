---
role: proof
locale: en
of_concept: dedekind-determinant-splitting
source_book: gtm059
source_chapter: "3. Complex Analytic Class Number Formulas"
source_section: "6"
---
Let $a_1, a_2, \dots, a_n$ be the elements of $G$. In the determinant
$$\det\left( f(a_i a_j^{-1}) \right)_{i,j=1}^n,$$
add the first row to each of the last $n-1$ rows. Then all elements of each new row are equal to $\sum_{k=1}^n f(a_k a_j^{-1}) = \sum_{a \in G} f(a)$. Factoring this common factor $\sum_{a \in G} f(a)$ out of each of the $n-1$ modified rows yields
$$\left( \sum_{a \in G} f(a) \right)^{n-1} \cdot \det(\text{reduced matrix}).$$

Combining with Theorem 6.1, which gives $\det(f(ab^{-1})) = \prod_{\chi \in \hat{G}} \sum_{a \in G} \chi(a) f(a)$, and noting that for the trivial character $\chi_0$ we have $\sum_{a \in G} \chi_0(a) f(a) = \sum_{a \in G} f(a)$, the factorization follows.
