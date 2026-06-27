---
role: proof
locale: en
of_concept: induced-map-theorem
source_book: gtm036
source_chapter: "5"
source_section: "5.8"
---

This theorem follows immediately from the preceding observations about the quotient map $Q: E \to E/F$.

If $F$ is a linear subspace of a linear topological space $E$, then for any open set $V$ in $E$, $Q^{-1}[Q[V]] = V + F$ is open in $E$. More generally, the sum of an open set and any set is open.

Now let $T: E \to G$ be linear with null space $F$, and let $S: E/F \to G$ be the induced map, so that $T = S \circ Q$. For any subset $W$ of $G$:

$$
T^{-1}[W] = (S \circ Q)^{-1}[W] = Q^{-1}[S^{-1}[W]].
$$

Since $Q$ is a quotient map, $S^{-1}[W]$ is open in $E/F$ if and only if $Q^{-1}[S^{-1}[W]] = T^{-1}[W]$ is open in $E$. This proves that $S$ is continuous if and only if $T$ is continuous.

In a similar manner, since $Q$ is both open and continuous, the openness of $S$ is equivalent to the openness of $T$: for an open set $U$ in $E$, we have $S[Q[U]] = T[U]$, and $Q[U]$ is open in $E/F$. Conversely, if $S$ is open and $V$ is open in $E/F$, then $T[Q^{-1}[V]] = S[V]$ is open.

Finally, if $T$ is both continuous and open, then $S$ is continuous and open, hence a homeomorphism; and since $S$ is a linear isomorphism onto $T[E]$, it is a topological isomorphism from $E/F$ onto $T[E]$.
