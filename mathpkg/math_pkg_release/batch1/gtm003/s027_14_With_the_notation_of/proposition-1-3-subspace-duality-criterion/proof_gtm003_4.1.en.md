---
role: proof
locale: en
of_concept: proposition-1-3-subspace-duality-criterion
source_book: gtm003
source_chapter: "4"
source_section: "1"
---

To prove the sufficiency of the condition, we have to show that the canonical bilinear form satisfies $(S_1)$ on $F \times G_1$. If $G_1$ is weakly dense in $G$ and $\langle x_0, y \rangle = 0$ for all $y \in G_1$, then the $\sigma(G, F)$-continuity of $y \rightarrow \langle x_0, y \rangle$ implies that $\langle x_0, y \rangle = 0$ for all $y \in G$, whence $x_0 = 0$ by $(S_1)$ for $\langle F, G \rangle$.

For the necessity of the condition, suppose that $\langle F, G \rangle$ induces a duality between $F$ and $G_1$. If $G_1$ were not dense in $(G, \sigma(G, F))$, then there exists a non-zero element $y_0 \in G$ not in the closure of $G_1$. By the Hahn-Banach theorem (or the bipolar theorem) in the weak topology, there exists $x_0 \in F$ such that $\langle x_0, y \rangle = 0$ for all $y \in G_1$ but $\langle x_0, y_0 \rangle \neq 0$. This contradicts $(S_1)$ for the restricted bilinear form on $F \times G_1$, since $x_0 \neq 0$ but $\langle x_0, y \rangle = 0$ for all $y \in G_1$. Hence $G_1$ must be $\sigma(G, F)$-dense in $G$.
