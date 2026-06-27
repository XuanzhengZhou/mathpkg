---
role: proof
locale: en
of_concept: banach-mazur-game-baire-determination
source_book: gtm002
source_chapter: "6"
source_section: "The Banach-Mazur Game"
---

**Proof.** Let $A = G \triangle P$, where $G$ is open and $P$ is of first category. If $G = \emptyset$, then $A = P$ is of first category, and by Theorem 6.1, player $(B)$ has a winning strategy.

If $G \neq \emptyset$, player $(A)$ can choose $I_1 \subset G$ as his first move. Then $I_1 \cap A = I_1 \triangle (I_1 \cap P)$, so $I_1 \cap B = I_1 \cap P$ is of first category. By Theorem 6.2, $(A)$ has a winning strategy.

Thus the outcome is determined solely by whether $A$ is of first or second category (equivalently for Baire sets, whether $G$ is empty or not). $\square$
