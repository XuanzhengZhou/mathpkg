---
role: proof
locale: en
of_concept: separability-of-descending-compact-sets
source_book: gtm047
source_chapter: "12"
source_section: "Homeomorphisms between Cantor sets"
---

Suppose not. Then $M_{\infty} = M_A \cup M_B$, where $M_A$ and $M_B$ are disjoint closed sets containing $M_{\infty} \cap A$ and $M_{\infty} \cap B$ respectively. The distance between $M_A \cup A$ and $M_B$ is positive; that is,
$$\inf \{ d(P, Q) \mid P \in M_A \cup A,\; Q \in M_B \} = \varepsilon_B > 0.$$
Similarly, the distance between $M_B \cup B$ and $M_A$ is positive, $= \varepsilon_A$. Let
$$\varepsilon = \frac{1}{2} \min \{ \varepsilon_A, \varepsilon_B \}.$$
Let
$$U_A = N(M_A, \varepsilon), \quad U_B = N(M_B, \varepsilon).$$
Then $U_A$ and $U_B$ are disjoint; they contain $M_A$ and $M_B$ respectively; and $U_A \cap B = U_B \cap A = \emptyset$.

Let $U = U_A \cup U_B$, and for each $i$, let $K_i = M_i - U$. Then $K_i \neq \emptyset$ for each $i$, because otherwise $M_i$ would lie in $U$ for some $i$, and $A$ and $B$ would be separable in $M_i$, which is false. Each $K_i$ is compact. And the sequence $K_1, K_2, \ldots$ is descending. It follows that $\bigcap_{i=1}^{\infty} K_i \neq \emptyset$. But this is impossible, because
$$\bigcap_{i=1}^{\infty} K_i = \bigcap_{i=1}^{\infty} [M_i \cap (X - U)] = M_{\infty} \cap (X - U) = \emptyset.$$
