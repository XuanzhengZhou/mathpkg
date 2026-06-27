---
role: proof
locale: en
of_concept: morse-type-numbers-dominate-betti-numbers
source_book: gtm033
source_chapter: "6"
source_section: "6.3"
---

# Proof of Morse Type Numbers Dominate Betti Numbers

Set $\delta_k = v_k - \beta_k$ for $k = 0, \ldots, n$. The Morse inequalities (part (a) of Theorem 3.4) state that for $0 \leqslant m \leqslant n$,

$$\sum_{k=0}^{m} (-1)^{k+m} v_k \geqslant \sum_{k=0}^{m} (-1)^{k+m} \beta_k.$$

Rearranging in terms of $\delta_k$, the inequality for $m = 0$ gives $\delta_0 \geqslant 0$. For $m = 1$, we obtain

$$v_1 - v_0 = \sum_{k=0}^{1} (-1)^{k+1} v_k \geqslant \sum_{k=0}^{1} (-1)^{k+1} \beta_k = \beta_1 - \beta_0,$$

which implies $\delta_1 \geqslant \delta_0 \geqslant 0$.

Continuing inductively, the Morse inequalities are equivalent to the chain of inequalities:

$$\begin{aligned}
\delta_0 &\geqslant 0, \\
\delta_1 &\geqslant \delta_0 \geqslant 0, \\
\delta_2 &\geqslant \delta_1 - \delta_0 \geqslant 0, \\
&\;\;\vdots \\
\delta_{m+1} &\geqslant \delta_m - \delta_{m-1} + \cdots + (-1)^m \delta_0 \geqslant 0.
\end{aligned}$$

In particular, each $\delta_k \geqslant 0$ for $k = 0, \ldots, n$. Therefore

$$v_k \geqslant \beta_k, \qquad k = 0, \ldots, n,$$

which is the statement to be proved. The same conclusion holds for Theorem 3.5 (the empty boundary case) by the same algebraic manipulation of the inequalities.
