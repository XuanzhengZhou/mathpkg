---
role: proof
locale: en
of_concept: closed-subspace-of-compact
source_book: gtm003
source_chapter: "0"
source_section: "8"
---

Let $X$ be compact and $A \subset X$ closed. Let $\{U_i\}_{i \in I}$ be an open cover of $A$ in the subspace topology, so $U_i = A \cap V_i$ with $V_i$ open in $X$. Then $\{V_i\}_{i \in I} \cup \{X \setminus A\}$ is an open cover of $X$. By compactness of $X$, there exists a finite subcover $\{V_{i_1}, \ldots, V_{i_n}, X \setminus A\}$ (where $X \setminus A$ may or may not be needed). Then $\{U_{i_1}, \ldots, U_{i_n}\}$ is a finite subcover of $A$, proving $A$ is compact.
