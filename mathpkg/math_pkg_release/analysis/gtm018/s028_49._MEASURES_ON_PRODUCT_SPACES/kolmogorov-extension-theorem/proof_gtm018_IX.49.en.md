---
role: proof
locale: en
of_concept: kolmogorov-extension-theorem
source_book: gtm018
source_chapter: "IX"
source_section: "49"
---

Define a measurable transformation $T_n$, from $X$ onto the measurable space $Y_n = \bigtimes_{i=1}^n X_i$, by

$$T_n(x_1, \cdots, x_n, x_{n+1}, \cdots) = (x_1, \cdots, x_n), \quad n = 1, 2, \cdots,$$

and write, for every measurable subset $A$ of $Y_n$, $\nu_n(A) = \mu(T_n^{-1}(A))$.

If $\{E_i\}$ is a decreasing sequence of sets in $F$ such that $0 < \epsilon \leq \mu(E_i)$, $i = 1, 2, \cdots$, then, for each fixed $i$, there is a positive integer $n$ and a Borel set $A_i$ in $Y_n$ such that $E_i = T_n^{-1}(A_i)$. Let $B_i$ be a closed subset of $A_i$ such that

$$\nu_n(A_i - B_i) \leq \frac{\epsilon}{2^{i+1}}.$$

If $F_i = \bigcap_{j=1}^i T_n^{-1}(B_j)$, then $\{F_i\}$ is a decreasing sequence of closed cylinders in $X$ (i.e., each $F_i$ is compact), and one verifies that $\mu(F_i) \geq \epsilon/2 > 0$, so each $F_i$ is non-empty. By compactness, $\bigcap_{i=1}^\infty F_i \neq \emptyset$, which implies $\bigcap_{i=1}^\infty E_i \neq \emptyset$. This establishes countable additivity of $\mu$ on $F$, and the Caratheodory extension theorem yields the unique extension to $S$.
