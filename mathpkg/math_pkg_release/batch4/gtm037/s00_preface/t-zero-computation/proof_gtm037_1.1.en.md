---
role: proof
locale: en
of_concept: t-zero-computation
source_book: gtm037
source_chapter: "1"
source_section: "1.1"
---

By Definition 1.7, the matrix of $T_0$ is:
\[
\begin{array}{cccc}
0 & 0 & 4 & 0 \\
0 & 1 & 0 & 0
\end{array}
\]

Take any tape description $F$ and any $e \in \mathbb{Z}$.

**(i)** Suppose $Fe = 0$. The row of the matrix beginning with $(0, 0)$ is $(0, 0, 4, 0)$. Since the third entry is $4$, the computation stops immediately at the initial configuration. The initial state is $0$ (the only state). Thus $\langle (F, 0, e) \rangle$ is a finite sequence of configurations starting from the initial state, with the final configuration having a matrix row with third entry $4$. This is a computation of $T_0$.

**(ii)** Suppose $Fe = 1$. The row of the matrix beginning with $(0, 1)$ is $(0, 1, 0, 0)$. By the definition of a computation step, since $w = 0$, we have $F' = F_0^e$, $d' = 0$, and $e' = e$. Thus the next configuration after $(F, 0, e)$ is $(F_0^e, 0, e)$.

Now at configuration $(F_0^e, 0, e)$, the scanned symbol is $F_0^e(e) = 0$ (since $F_0^e$ was defined to have value $0$ at $e$). The row of the matrix beginning with $(0, 0)$ is $(0, 0, 4, 0)$. Since the third entry is $4$, the computation stops at this configuration.

Therefore $\langle (F, 0, e), (F_0^e, 0, e) \rangle$ is a finite sequence of configurations starting from the initial state $0$, with each adjacent pair forming a valid computation step, and ending at a configuration whose matrix row specifies action $4$ (stop). This is exactly a computation of $T_0$.

*Note: The original statement in the source text is truncated; this proof has been reconstructed from the definition of $T_0$ using mathematical reasoning.*
