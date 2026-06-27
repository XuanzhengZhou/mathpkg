---
role: proof
locale: en
of_concept: inverse-in-whitehead-group
source_book: gtm010
source_chapter: "6"
source_section: "6. The Whitehead group of a CW complex"
---

\begin{proof}
We compute:
\begin{align*}
[2M_D, L] + [K, L] &= [2M_D \cup_L K, L] \\
&= [(M_D \cup_L K) \cup M'_D, L] \\
&= [M_{iD} \cup M'_D, L] \qquad \text{where } i: L \hookrightarrow K.
\end{align*}

Since $iD \simeq 1_K$, by (5.5) we have $M_{iD} \wedge K \times I$ rel $(K \times 0) \cup K$. Hence by (5.3'):
\begin{align*}
&= [K \times I \cup M'_D, L] \\
&= [L \times I \cup M'_D, L] \qquad \text{since } K \times I \searrow (L \times I \cup K \times 0) \\
&= [L \times [-1, 1], L] \qquad \text{since } M'_D \searrow L \times [-1, 0] \\
&= [L, L] = 0 \qquad \text{since } L \times [-1, 1] \searrow L \equiv L \times 1.
\end{align*}

Thus $[2M_D, L] = -[K, L]$.
\end{proof}
