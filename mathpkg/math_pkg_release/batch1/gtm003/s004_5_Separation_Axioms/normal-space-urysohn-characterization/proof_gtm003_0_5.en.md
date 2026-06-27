---
role: proof
locale: en
of_concept: normal-space-urysohn-characterization
source_book: gtm003
source_chapter: "0"
source_section: "5"
---

The original text in this section mentions the theorem without providing a complete proof; the text is truncated mid-sentence. The standard proof (Urysohn's Lemma) proceeds as follows: For a normal space $X$ and disjoint closed sets $A, B$, let $U_1 = X \setminus B$. By normality, there exists an open set $U_{1/2}$ such that $A \subset U_{1/2} \subset \overline{U}_{1/2} \subset U_1$. Iteratively, one constructs open sets $U_r$ for all dyadic rationals $r \in [0,1]$ with the property that $r < s$ implies $\overline{U}_r \subset U_s$. Define $f(x) = \inf\{r : x \in U_r\}$ (with $f(x) = 1$ if $x$ belongs to no $U_r$). Then $f$ is continuous, $f = 0$ on $A$, and $f = 1$ on $B$. Conversely, if such a separating function exists, setting $U = f^{-1}([0, 1/2))$ and $V = f^{-1}((1/2, 1])$ yields disjoint neighborhoods of $A$ and $B$.
