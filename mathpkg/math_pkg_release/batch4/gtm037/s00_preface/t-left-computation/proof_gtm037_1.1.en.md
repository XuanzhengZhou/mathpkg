---
role: proof
locale: en
of_concept: t-left-computation
source_book: gtm037
source_chapter: "1"
source_section: "1.1"
---

By Definition 1.5, the matrix of $T_{\text{left}}$ is:
\[
\begin{array}{cccc}
0 & 0 & 3 & 1 \\
0 & 1 & 3 & 1 \\
1 & 0 & 4 & 1 \\
1 & 1 & 4 & 1
\end{array}
\]

Take any tape description $F$ and any $e \in \mathbb{Z}$. Consider the configuration $(F, 0, e)$. The scanned symbol is $Fe$, which is either $0$ or $1$. In either case, the row of the matrix beginning with $(0, Fe)$ is $(0, Fe, 3, 1)$. By the definition of a computation step, since $w = 3$, we have $F' = F$, $d' = 1$, and $e' = e + 1$. Thus the next configuration is $(F, 1, e + 1)$.

Now at configuration $(F, 1, e + 1)$, the scanned symbol is $F(e+1)$, which is either $0$ or $1$. In either case, the row of the matrix beginning with $(1, F(e+1))$ is $(1, F(e+1), 4, 1)$. Since the third entry is $4$, the computation stops at this configuration.

Therefore $\langle (F, 0, e), (F, 1, e + 1) \rangle$ is a finite sequence of configurations starting from the initial state $0$, with each adjacent pair forming a valid computation step, and ending at a configuration whose matrix row specifies action $4$ (stop). This is exactly a computation of $T_{\text{left}}$.
