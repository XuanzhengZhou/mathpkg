---
role: proof
locale: en
of_concept: noether-basis-theorem
source_book: gtm031
source_chapter: "IV"
source_section: "1-6"
---
There exists a complement $\mathfrak{S}'$ of $\mathfrak{S}$ spanned by a subset $D = (e_k)$ of $B$. Let $C = (e_j)$ be the complement of $D$ in $B$. Then each $e_j = f_j - u_j$ where $f_j \in \mathfrak{S}$ and $u_j \in \mathfrak{S}'$ and, as we proceed to show, $(f_j)$ is a basis for $\mathfrak{S}$. The set $(f_j)$ is linearly independent, for let $\sum \beta_j f_j = 0$. Then $\sum \beta_j e_j + \sum \beta_j u_j = 0$; hence every $\beta_j = 0$ by the linear independence of the $e_j$. The set $(f_j)$ generates $\mathfrak{S}$; for if $y \in \mathfrak{S}$, then $y = \sum \beta_j e_j + \sum \gamma_k e_k = \sum \beta_j f_j - \sum \beta_j u_j + \sum \gamma_k e_k$. Then $y - \sum \beta_j f_j \in \mathfrak{S}'$, and hence $y - \sum \beta_j f_j = 0$. We note finally that, if $e_j$ and $e_{j'}$ are distinct elements in $C$, then $f_j \neq f_{j'}$. Otherwise $e_j - e_{j'} \in \mathfrak{S}'$, contrary to the fact that $B$ is a basis. We therefore see that the mapping $e_j \to f_j$ is 1-1 and this concludes the proof.

