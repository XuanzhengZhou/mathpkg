---
role: proof
locale: en
of_concept: antoine-2-sphere-theorem
source_book: gtm047
source_chapter: "18"
source_section: "18 (Antoine's Necklace)"
---

Let $B_C$ be a broken line from a fixed basepoint $Q_C$ to $Bd C$ for each component $C$ of $T_n$, constructed so that $B_C \cap T_n = \{Q_C\}$ (this is possible because $U - T_n$ is connected, and each point of $\text{Bd } T_n$ is a limit point of $U - T_n$). Let $B$ be the union of the broken lines $B_C$. Then $B$ has a polyhedral 3-cell neighborhood $N$, such that for each component $C$ of $T_n$, $N \cap \text{Bd } C$ is a 2-cell. Let $A_n = \text{Bd } N - \text{Int } T_n$.

Suppose inductively that we have a multiple annulus $A_m$ ($m \geqslant n$) such that $A_m$ spans $T_m$ in $U$. There is then a multiple annulus $A_{m+1}$, containing $A_m$ and spanning $T_{m+1}$ in $U$, such that $A_{m+1} - T_m = A_m - T_m$; in each component of $T_m$ we insert a multiple annulus, by the same sort of process used in defining $A_n$. Thus there is an ascending sequence $A_1, A_2, \ldots$ of multiple annuli, such that if

$$A = \bigcup_{i > n} A_i,$$

then $A - A_i \subset T_i$ for each $i \geqslant n$. It follows that $\bar{A} = A \cup \mathcal{Q}$. Let

$$S = \bar{A} = A \cup \mathcal{Q}.$$

To see that $S$ is a 2-sphere, copy the structure of the sets $A_i$ with sets $A_i'$ in a 2-sphere $S^2$, in such a way that the maximum diameter of the components of $S^2 - A_i'$ approaches $0$ as $i \to \infty$. Let

$$A' = \bigcup_{i > n} A_i'.$$

Now define a homeomorphism $\phi: A \leftrightarrow A'$, by first defining a homeomorphism $\phi_n: A_n \leftrightarrow A_n'$, and then extending $\phi_n$, a step at a time, to the successive annuli. This homeomorphism demonstrates that $S$ is indeed a 2-sphere.
