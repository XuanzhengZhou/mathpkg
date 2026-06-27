---
role: proof
locale: en
of_concept: mean-of-nj-in-sequence-space
source_book: gtm040
source_chapter: "2"
source_section: "6"
---

\begin{proof}
Using the indicator functions $u_j^{(n)}$ defined by $u_j^{(n)}(\omega) = 1$ if $x_n(\omega) = j$ and $0$ otherwise, we have $n_j = \sum_{n=0}^{\infty} u_j^{(n)}$. Then
\begin{align*}
M[n_j] &= M\left[\sum_{n=0}^{\infty} u_j^{(n)}\right] \\
&= \sum_{n=0}^{\infty} M[u_j^{(n)}] \quad \text{(by Corollary 1-46, monotone convergence for means)} \\
&= \sum_{n=0}^{\infty} \int_{\Omega} u_j^{(n)} \, d\mu \\
&= \sum_{n=0}^{\infty} \int_{\{\omega \mid x_n(\omega) = j\}} 1 \, d\mu \\
&= \sum_{n=0}^{\infty} \Pr[x_n = j].
\end{align*}
\end{proof}
