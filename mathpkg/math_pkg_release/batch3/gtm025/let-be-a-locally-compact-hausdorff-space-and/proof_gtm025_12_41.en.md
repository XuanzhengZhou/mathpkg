---
role: proof
locale: en
of_concept: "let-be-a-locally-compact-hausdorff-space-and"
source_book: gtm025
source_chapter: "The Lebesgue Integral"
source_section: "12.41"
---

Let $F$ be any nonvoid compact subset of $X$. Use (12.39.ii) to find sequences $(U_n)$ and $(V_n)$ of open sets containing $F$ such that $\mu(U_1) < \infty, \nu(V_1) < \infty, \mu(U_n) \to \mu(F),$ and $\nu(V_n) \to \nu(F)$. For each $n \in N$, set $W_n = \bigcap_{k=1}^{n} (U_k \cap V_k)$. Then each $W_n$ is open, $W_1 \supset W_2 \supset \cdots \supset F$, $\nu(W_n) \to \nu(F)$, and $\mu(W_n) \to \mu(F)$. For each

Proof. Let $E$ be in $\mathcal{A}$ and suppose that $\mu(E) < \infty$. Since $\mu$ is regular, there exist sequences of sets $(F_n)$ and $(U_n)$ such that $F_n \subset E \subset U_n$, each $F_n$ is compact, each $U_n$ is open, $\mu(F_n) \rightarrow \mu(E)$, and $\mu(U_n) \rightarrow \mu(E)$. Let $A = \bigcup_{n=1}^{\infty} F_n$ and $B = \bigcap_{n=1}^{\infty} U_n$. Then $A$ and $B$ are Borel sets, $A \subset E \subset B$, $\mu(A) = \mu(E) = \mu(B)$, and $\mu(B \cap A') = 0$. It follows from (12.35) and (12.41) that $\iota(A) = \iota(B)$ and $\iota(B \cap A') = 0$. Therefore, since $\iota$ is complete, $E = A \cup [E \cap (B \cap A')] \in \mathcal{M}_i$. This argument proves:

$$E \in \mathcal{A} \text{ and } \mu(E) < \infty \text{ imply } E \in \mathcal{M}_i. \tag{1}$$

Repeating the above argument with the roles of $\mu$ and $\iota$ reversed, we have

$$E \in \mathcal{M}_i \text{ and } \iota(E) < \infty \text{ imply } E \in \mathcal{A}. \tag{2}$$

Next consider any $E$ in $\mathcal{A}$ and any compact set $F \subset X$. By hypothesis we have $E \cap F \in \mathcal{A}$, and of course $\mu(E \cap F) < \infty$. Therefore $E \cap F$ is in $\mathcal{M}_i$ for all compact sets $F$. Applying (10.31.iv), we infer that $E \in \mathcal{M}_i$, and so we have proved that $A \subset \mathcal{M}_i$. A very similar argument proves the reversed inclusion,
