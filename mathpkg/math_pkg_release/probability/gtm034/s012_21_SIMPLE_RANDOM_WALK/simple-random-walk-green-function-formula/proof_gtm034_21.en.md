---
role: proof
locale: en
of_concept: simple-random-walk-green-function-formula
source_book: gtm034
source_chapter: "V"
source_section: "21"
---

The shortest proof of (a) consists of verifying, by matrix multiplication, that the matrix on the right in (a) is indeed the inverse of $2(N+2)(I_N - Q_N)$. Since $g_N(x,y) = \sum_{n=0}^{\infty} Q_N^n(x,y) = (I_N - Q_N)^{-1}(x,y)$, this verification establishes the formula. The computation follows from the spectral theorem for symmetric matrices: diagonalizing $Q_N$ using the eigenvalues $\lambda_k$ and eigenvectors $v_k$ from P1 yields $g_N(x,y) = \sum_{k=0}^{N} \frac{v_k(x) v_k(y)}{1 - \lambda_k}$. Substituting the explicit expressions for $\lambda_k$ and $v_k$ and using trigonometric sum identities leads to the stated formula involving $R$.

Once (a) is established, (b) follows from the definitions in D1. Specifically,
$$R_N(x) = \sum_{k=1}^{\infty} \sum_{y=0}^{N} g_N(x,y) P(y, N+k).$$
For simple random walk, $P(y,N+k) = \frac{1}{2}$ only when $y=N$ and $k=1$, so the sum collapses to a single term involving $g_N(x,N)$. Evaluating $g_N(x,N)$ using (a) yields $R_N(x) = \frac{x+1}{N+2}$. The formula for $L_N$ follows by symmetry.
