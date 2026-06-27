---
role: proof
locale: en
of_concept: stopped-martingale-property
source_book: gtm017
source_chapter: "VIII"
source_section: "b"
---
$X_n^T = \sum_{j=0}^{n-1} X_j I_{\{T=j\}} + X_n I_{\{T \geq n\}}$. For a martingale:
$$E[X_{n+1}^T - X_n^T | \mathcal{B}_n] = E[I_{\{T \geq n+1\}}(X_{n+1} - X_n) | \mathcal{B}_n] = I_{\{T \geq n+1\}} E[X_{n+1} - X_n | \mathcal{B}_n] = 0.$$

Integrability: $|X_n^T| \leq |X_0| + \cdots + |X_n|$, so $E|X_n^T| < \infty$. For supermartingales, the equality becomes $\leq 0$.
