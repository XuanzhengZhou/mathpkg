---
role: proof
locale: en
of_concept: corollary-with-assumptions-notations-theorem-decomposition
source_book: gtm029
source_chapter: "Appendix"
source_section: "5"
---

Assume that $R' \mathfrak{A} \cap \mathfrak{o} = \mathfrak{A}$ and let $x$ be any element of $\mathfrak{A} : \mathfrak{o} t_1$. Then $xt_1 = a \in \mathfrak{A}$, $xt_2 = a \cdot t_2 / t_1 \in R' \mathfrak{A} \cap \mathfrak{o} = \mathfrak{A}$, and so

$$x \in \mathfrak{A} : (\mathfrak{o} t_1 + \mathfrak{o} t_2) = \mathfrak{A} : \mathfrak{m},$$

which proves (27).

Conversely, assume that (27) holds true and let $x$ be any element of $R' \mathfrak{A} \cap \mathfrak{o}$. Then $x = \sum_{i=0}^{n} a_i \left( \frac{t_2}{t_1} \right)^i, a_i \in \mathfrak{A}$. We see that $a_n$ is divisible by $t_1$ in $\mathfrak{o}$, say $a_n = t_1 b_n$, and since $a_n \in \mathfrak{A}$ it follows from (27) that $t_2 b_n$ also belongs to $\mathfrak{A}$. If, then, we set $t_2 b_n = b_{n-1}$ we find

$$x = \sum_{i=0}^{n-2} a_i \left( \frac{t_2}{t_1} \right)^i + (a_{n-1} + b_{n-1}) \left( \frac{t_2}{t_1} \right)^{n-1}.$$

This is a new expression of $x$ as a polynomial in $t_2 / t_1$, with coefficients which still belong to $\mathfrak{A}$, but the degree of the polynomial is now at most $n-1$. Continuing the reduction of degree we arrive at the desired conclusion.
