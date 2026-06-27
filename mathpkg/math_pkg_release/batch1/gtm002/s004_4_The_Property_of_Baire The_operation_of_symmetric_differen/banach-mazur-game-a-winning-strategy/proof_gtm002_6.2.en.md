---
role: proof
locale: en
of_concept: banach-mazur-game-a-winning-strategy
source_book: gtm002
source_chapter: "6"
source_section: "The Banach-Mazur Game"
---

**Proof.** If there exists $I_1 \subset I_0$ such that $I_1 \cap B$ is of first category, then $(A)$ can start by choosing $I_1$. By applying the strategy of Theorem 6.1 with $A$ playing the role of $(B)$ against the first-category set $I_1 \cap B$, player $(A)$ can ensure that $\bigcap_{n=1}^{\infty} I_n \cap (I_1 \cap B) = \emptyset$, i.e., $\bigcap I_n \subset I_1 \cap A \subset A$. Hence $(A)$ wins.

Conversely, suppose $(A)$ has a winning strategy. By modifying the strategy to always choose $I_{2n+1}$ as if $I_{2n}$ had been half as long, $(A)$ can ensure that $\bigcap I_n$ consists of a single point of $A$. This defines a winning strategy for the second player in the game $\langle I_1 \cap B, I_1 \cap A \rangle$ for some initial move $I_1$. By Theorem 6.1, this implies $I_1 \cap B$ is of first category. $\square$
