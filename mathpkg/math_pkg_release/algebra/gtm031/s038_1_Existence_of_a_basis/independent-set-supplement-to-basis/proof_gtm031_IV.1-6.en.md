---
role: proof
locale: en
of_concept: independent-set-supplement-to-basis
source_book: gtm031
source_chapter: "IV"
source_section: "1-6"
---
It suffices to consider the case in which both bases $B$ and $C$ are infinite. Here the following argument due to Lowig can be applied. Express each $e_i$ of $B$ in terms of the $f_k$ of $C$ as
$$e_i = \beta_1 f_{k_1} + \beta_2 f_{k_2} + \cdots + \beta_m f_{k_m}$$
where the $\beta_j \neq 0$. Now every $f_k$ occurs in some such expression; for if a particular $f_k$ does not occur, then, since this $f_k$ is a linear combination of the $e$'s and each $e$ is a linear combination of $f$'s $\neq f_k$, $f_k$ is a linear combination of $f$'s $\neq f_k$. This contradicts the linear independence of the $f$'s.

We can now define a single-valued mapping $\phi$ of the set $C$ into the set $B$. Let $f_k \in C$ and let $e_i \equiv \phi(f_k)$ be one of the $e$'s in $B$ whose expression involves $f_k$. We thus obtain a single-valued mapping of the whole of $C$ into $B$. Let $B' = \phi(C)$ be the image set. If $e_{i'} \in B'$, the inverse image $\phi^{-1}(e_{i'})$ consists of those $f_k$ which occur in the expression for $e_{i'}$. Thus $\phi^{-1}(e_{i'})$ is a finite set. Now we have a 1-1 correspondence between the set $B'$ and the collection $\Gamma$ of inverse images $\phi^{-1}(e_{i'})$. The collection $\Gamma$ gives a decomposition of the set $C$ into non-overlapping finite sets. Moreover, since $C$ is infinite, $\Gamma$ is infinite. It follows easily from standard theorems in the theory of cardinal numbers that $C$ and $\Gamma$ have the same cardinal number. Hence the cardinal number of $B'$ is the same as that of $C$ and so the cardinal number of $B$ is greater than or equal to that of $C$.

