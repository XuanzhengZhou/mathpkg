---
role: proof
locale: en
of_concept: set-valued-algebraic-functor-has-coequalizers
source_book: gtm026
source_chapter: "1"
source_section: "1.31"
---

**Proof.** Let $f, g: A_1 \longrightarrow A_2$ be admissible morphisms in $\mathcal{A}$. Let $S = \{(a_1 f, a_1 g) : a_1 \in A_1 U\}$. Let $R$ be the intersection of all congruences (defined in 1.11) on $A_2$ containing $S$. We argue that $R$ is a congruence as follows: Let $(R_i : i \in I)$ be the set of all congruences on $A_2$ which contain $S$. Define a diagram scheme $\Delta$ with $N(\Delta) = I \cup \{t, t'\}$ where $t, t' \notin I$ and such that $\Delta(i, j)$ has exactly one element if $i \in I$ and $j$ is appropriately chosen. The intersection of congruences is formed by taking the limit of this diagram, and since $U$ creates limits (being algebraic), this limit exists in $\mathcal{A}$ and the intersection is again a congruence.

Since $f \cdot h = g \cdot h$, $S$ is a subset of $E$, so $R$ is also a subset of $E$, and $\bar{p} \cdot h = \bar{q} \cdot h$ inducing the desired unique $\psi$. $\psi$ is admissible by 2.1.56. $\square$
