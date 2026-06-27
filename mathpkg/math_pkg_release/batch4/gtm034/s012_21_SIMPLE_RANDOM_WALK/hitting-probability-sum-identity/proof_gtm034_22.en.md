---
role: proof
locale: en
of_concept: hitting-probability-sum-identity
source_book: gtm034
source_chapter: "V"
source_section: "22"
---

The argument is based on the identities (valid for $0 \leq x \leq N$, $k \geq 0$):
$$R_N(x,k) = \sum_{y=0}^{N} g_N(x,y) P(y, N+k), \quad L_N(x,k) = \sum_{y=0}^{N} g_N(x,y) P(y, -k),$$
which follow from first-entrance decomposition.

For part (a), the left-hand side becomes
$$\sum_{k=1}^{\infty} [R_N(x,k) + L_N(x,k)] = \sum_{y=0}^{N} g_N(x,y) \left[ 1 - \sum_{s=0}^{N} P(y,s) \right].$$
Using the identity $\sum_{y=0}^{N} g_N(x,y) P(y,s) = g_N(x,s) - \delta(x,s)$ for $x,s \in [0,N]$ (which follows from $g_N = \sum_{n=0}^{\infty} Q_N^n$ and $Q_N^{n+1} = Q_N^n Q_N$), one obtains
$$\sum_{k=1}^{\infty} [R_N(x,k) + L_N(x,k)] = \sum_{y=0}^{N} g_N(x,y) - \sum_{s=0}^{N} g_N(x,s) + \sum_{s=0}^{N} \delta(x,s) = 1.$$

For part (b), the left-hand side is transformed into
$$\sum_{y=0}^{N} g_N(x,y) \left[ \sum_{k=1}^{\infty} (N+k) P(y, N+k) - \sum_{k=1}^{\infty} k P(y, -k) \right]$$
$$= \sum_{y=0}^{N} g_N(x,y) \left[ \sum_{j=-\infty}^{\infty} j P(y,j) - \sum_{j=0}^{\infty} j P(y,j) \right].$$
Since $\sum_j j P(y,j) = y$ when $\mu = 0$, the expression reduces to
$$\sum_{y=0}^{N} y g_N(x,y) - \sum_{j=0}^{\infty} j g_N(x,j) + \sum_{j=0}^{\infty} j \delta(x,j) = x.$$
