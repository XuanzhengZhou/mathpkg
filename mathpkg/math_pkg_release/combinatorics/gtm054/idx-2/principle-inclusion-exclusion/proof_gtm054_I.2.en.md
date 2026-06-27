---
role: proof
locale: en
of_concept: principle-inclusion-exclusion
source_book: gtm054
source_chapter: "I"
source_section: "2"
---

It suffices to prove (a), as (b) follows by duality.

By E8(c), $s^*(A)$ represents the number of vertices which belong to every block in $A$ but to no other block. Thus the number of vertices belonging to precisely $r$ blocks is $\sum_{|A|=r} s^*(A)$.

Applying Proposition E6 (Möbius inversion) to $s^*$ (with the roles of $V$ and $E$ interchanged, and treating $s^*$ as a selection on $\mathcal{P}(E)$):

\begin{align*}
\sum_{|A|=r} s^*(A) &= \sum_{|A|=r} \sum_{C \in \mathcal{P}(E)} (-1)^{|C+A|}[A, C] \bar{s}^*(C) \\
&= \sum_{|C| \geq r} \left( \sum_{|A|=r} (-1)^{|C+A|}[A, C] \right) \bar{s}^*(C).
\end{align*}

For a fixed $C$ of size $c \geq r$, the inner sum counts subsets $A$ of size $r$ with $A \subseteq C$ with alternating signs. There are $\binom{c}{r}$ such subsets, each having $|C+A| = c - r$, so:

$$\sum_{|A|=r} (-1)^{|C+A|}[A, C] = (-1)^{c-r} \binom{c}{r}.$$

Substituting and letting $i = c - r = |C| - r$:

\begin{align*}
\sum_{|A|=r} s^*(A) &= \sum_{c=r}^{|E|} (-1)^{c-r} \binom{c}{r} \sum_{|C|=c} \bar{s}^*(C) \\
&= \sum_{i=0}^{|E|-r} (-1)^i \binom{r+i}{i} \sum_{|C|=r+i} \bar{s}^*(C).
\end{align*}

This is exactly the claimed formula. Part (b) follows by applying (a) to the dual system $\Lambda^*$ and interpreting the result in terms of $\bar{s}$ via E8(b) and the fact that $s^{**} = s$.
