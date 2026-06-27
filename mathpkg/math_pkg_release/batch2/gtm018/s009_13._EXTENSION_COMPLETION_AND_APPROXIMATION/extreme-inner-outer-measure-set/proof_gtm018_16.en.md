---
role: proof
locale: en
of_concept: extreme-inner-outer-measure-set
source_book: gtm018
source_chapter: "III. Extension of Measures"
source_section: "§16. Non Measurable Sets"
---

Write $A = B \cup C$ as in Theorem C ($B$ has even $n$, $C$ odd $n$). Let $E_0$ be the Vitali set from Theorem D and set $M = E_0 + B$.

If $F$ is Borel with $F \subset M$, then $D(F)$ contains no element of $C$ (elements of $M$ differ by elements of $B$, and $B$ has only even $n$ while $C$ has odd $n$). By Theorem B, $\mu(F) = 0$, so $\mu_*(M) = 0$. Similarly $\mu_*(M') = 0$ where $M' = E_0 + C$.

For any measurable $E$, both $\mu_*(M \cap E) = 0$ and $\mu_*(M' \cap E) = 0$, which implies $\mu^*(M \cap E) = \bar{\mu}(E)$.
