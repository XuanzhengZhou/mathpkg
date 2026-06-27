---
role: proof
locale: en
of_concept: character-of-regular-representation
source_book: gtm042
source_chapter: "2"
source_section: "2.4"
---

The regular representation has as its space a vector space $\mathbb{R}$ with basis $(e_t)_{t \in G}$ indexed by the elements of $G$, and the action is given by $\rho_s(e_t) = e_{st}$ for $s, t \in G$.

For $s = 1$, the matrix of $\rho_1$ is the identity matrix of size $g \times g$, so its trace is $\operatorname{Tr}(\rho_1) = \dim(\mathbb{R}) = g$.

For $s \neq 1$, the transformation $\rho_s$ sends each basis vector $e_t$ to $e_{st}$. Since $s \neq 1$, we have $st \neq t$ for all $t \in G$, which means that all diagonal entries of the matrix of $\rho_s$ are zero. Consequently, $\operatorname{Tr}(\rho_s) = 0$.

Thus $r_G(1) = g$ and $r_G(s) = 0$ for $s \neq 1$. $\square$
