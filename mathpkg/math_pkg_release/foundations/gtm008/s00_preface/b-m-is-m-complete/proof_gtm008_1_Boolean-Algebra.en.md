---
role: proof
locale: en
of_concept: b-m-is-m-complete
source_book: gtm008
source_chapter: "1"
source_section: "Boolean Algebra"
---

**Proof.** If $a, b \in |B| \cap M$, then $a \cup b$, $a \cap b$, and $X - a$ are all in $M$ (by separation/replacement in $M$), and their regular-open closures (needed for the Boolean operations in the regular-open algebra) are also in $M$. Consequently, if $a, b \in |\mathbf{B}| \cap M$, then $a + b \in |\mathbf{B}| \cap M$, $ab \in |\mathbf{B}| \cap M$, and $-a \in |\mathbf{B}| \cap M$. Since $0, 1 \in M$, $\mathbf{B}^M$ is a subalgebra of $\mathbf{B}$.

If $A \subseteq |\mathbf{B}| \cap M$ and $A \in M$, then since $\mathbf{B}$ is complete and $M$ is a model of ZF, $\sum_{a \in A} a \in |\mathbf{B}| \cap M$. Thus $\mathbf{B}^M$ is $M$-complete.
