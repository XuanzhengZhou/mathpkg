---
role: proof
locale: en
of_concept: antoine-path-contraction-theorem
source_book: gtm047
source_chapter: "18"
source_section: "18 (Antoine's Necklace)"
---

We may suppose that $p$ is PL, and that there is a PL contraction

$$\phi: [0, 1]^2 \rightarrow \mathbf{R}^3 - \mathcal{Q}$$

of $p$. If it were true that $|\phi| \cap T_n \neq \varnothing$ for each $n$, then it would follow that $|\phi| \cap \mathcal{Q} \neq \varnothing$, which is false. Therefore

$$|\phi| \cap T_n = \varnothing$$

for some $n$. Let $C$ be a component of $T_{n-1}$; and let

$$T'_1 = C, \quad T'_2 = C \cap T_n.$$

Then $T'_1$ and $T'_2$ are related in the same way as $T_1$ and $T_2$; in fact, there is a similarity $T_1 \leftrightarrow T'_1$, $T_2 \leftrightarrow T'_2$. It follows by the preceding theorem that there is a contraction $\phi'$, of $p$ onto $e$ in $\mathbf{R}^3 - C$, such that $|\phi'| - |\phi|$ lies in a small neighborhood of $C$, and hence intersects no other component of $T_{n-1}$. Therefore, in a finite number of steps, we get a contraction of $p$ in $\mathbf{R}^3 - T_{n-1}$. By induction, $p$ is contractible in $\mathbf{R}^3 - T_1$.
