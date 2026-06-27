---
role: proof
locale: en
of_concept: ring-direct-sum-decomposition
source_book: gtm028
source_chapter: "III"
source_section: "§13"
---

Since $R_i R_j = (0)$ for $i \neq j$, we have $R_i R \subset R_i R_i + \sum_{j \neq i} R_i R_j = R_i^2 \subset R_i$, and similarly $R R_i \subset R_i$, showing $R_i$ is an ideal. For directness: $R_i \cap \sum_{j \neq i} R_j = (0)$ since any element in this intersection multiplies to zero with itself. The relation $R_i R_j = (0)$ implies that each element of $R_i$ is a zero divisor unless $R_j = (0)$ for $j \neq i$.

Existence of unique $e_i$ satisfying $1 = e_1 + \cdots + e_n$ with $e_i \in R_i$ follows from the direct sum decomposition, and $e_i e_j = 0$ for $i \neq j$ since $R_i R_j = (0)$. Multiplying by $e_i$ gives $e_i = e_i \cdot 1 = e_i(e_1 + \cdots + e_n) = e_i^2$, so $e_i^2 = e_i$. If $c \in R_i$, then $c = c \cdot 1 = c(e_1 + \cdots + e_n) = ce_i$, and hence also $R_i = Re_i$.

For an ideal $\mathfrak{A}$: multiplying $R = R_1 \oplus \cdots \oplus R_n$ by $\mathfrak{A}$ gives $\mathfrak{A} = R\mathfrak{A} = R_1\mathfrak{A} \oplus \cdots \oplus R_n\mathfrak{A}$, and $R_i\mathfrak{A}$ is an ideal in $R_i$.

If $\mathfrak{A}$ is primary with $\mathfrak{A} \neq R$, then not every $R_iT$ can be $(0)$. Since no power of $e_iT$ can be zero, it cannot be a zero-divisor in $R/\mathfrak{A}$ (since in a primary ring, every non-zero-divisor is a unit), forcing all other $R_jT = (0)$.
