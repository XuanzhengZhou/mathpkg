---
role: exercise
locale: en
chapter: "8"
section: "2"
exercise_number: "8.55a"
---

In three-valued logic, the truth values are $0$ (falsity), $1$ (truth), and $2$ (indeterminate). The truth tables for $\neg$ and $\rightarrow$ are as follows:

$$\begin{array}{c|c|c|c}
\varphi & \neg\varphi & & \varphi \rightarrow \psi \\
\hline
0 & 1 & & 1 \text{ if } \varphi \leq \psi \text{ or } (\varphi=2 \text{ and } \psi=2)\\
1 & 0 & & \text{ with value } 0 \text{ when } \varphi=1, \psi=0\\
2 & 2 & & \text{ and } 2 \text{ otherwise}
\end{array}$$

More precisely:
$$\begin{array}{c|ccc}
\rightarrow & 0 & 1 & 2 \\
\hline
0 & 1 & 1 & 1 \\
1 & 0 & 1 & 2 \\
2 & 0 & 2 & 2
\end{array}$$

and $\neg 0 = 1$, $\neg 1 = 0$, $\neg 2 = 2$.

(a) Show that the following sentence is not always true in three-valued logic, but is never false:

$$[\varphi \rightarrow (\psi \rightarrow \chi)] \rightarrow [(\varphi \rightarrow \psi) \rightarrow (\varphi \rightarrow \chi)]$$
