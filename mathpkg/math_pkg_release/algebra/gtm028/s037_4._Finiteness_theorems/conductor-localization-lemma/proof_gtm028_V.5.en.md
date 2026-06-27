---
role: proof
locale: en
of_concept: conductor-localization-lemma
source_book: gtm028
source_chapter: "V"
source_section: "§5. The conductor of an integral closure"
---

(1) Since $A'$ is integral over $A$, the localization $A'_S$ is integral over $A_S$. Conversely, if $x/s \in F$ (with $s \in S$) is integral over $A_S$, then clearing denominators yields that $x$ is integral over $A$, hence $x \in A'$, so $x/s \in A'_S$. Thus $A'_S$ is exactly the integral closure of $A_S$.

(2) If $z \in \mathfrak{f} \cap S$, then $z \in A$ and $zA' \subset A$. Hence $A' \subset (1/z)A \subset A_S$, so $A'_S = A_S$ and $A_S$ is integrally closed.

(3) Suppose $A' = \sum_{i=1}^n A u_i$ is a finite $A$-module. Then $A'_S = \sum_i A_S u_i$. For any $z/s \in \mathfrak{f} \cdot A_S$ (with $z \in \mathfrak{f}$), we have $(z/s) A'_S = (z/s) \sum_i A_S u_i \subset \sum_i A_S (z u_i) \subset A_S$ since $z u_i \in A$. Hence $\mathfrak{f} \cdot A_S$ is contained in the conductor of $A_S$ in $A'_S$. Conversely, if $y \in A_S$ belongs to the conductor of $A_S$ in $A'_S$, then $y u_i \in A_S$ for each $i$, so $y = z/s$ with $z \in \mathfrak{f}$. Thus the conductor of $A_S$ is exactly $\mathfrak{f} \cdot A_S$.

(4) If $A_S$ is integrally closed, then $A'_S = A_S$ by (1), so the conductor is the unit ideal.
