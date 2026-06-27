---
role: proof
locale: en
of_concept: convergence-conditional-probabilities
source_book: gtm017
source_chapter: "V"
source_section: "c"
---
It suffices to prove $P(A|\mathcal{C}_n) \to I_A(w)$ almost everywhere for $A \in \mathcal{C}$ (where $\mathcal{C}$ is the union closure). For any $\varepsilon, \delta > 0$, choose $B \in \mathcal{C}_k$ approximating $A$ within $\varepsilon\delta/2$. On $B$, construct sets $F_k^{(j)}$ where $P(A|\mathcal{C}_n)$ is close to 1 for $n \geq k+j-1$. Collecting estimates shows $P(A|\mathcal{C}_n) \to 1$ on $A$ and $\to 0$ on $\bar{A}$, both up to arbitrarily small exceptional sets.
