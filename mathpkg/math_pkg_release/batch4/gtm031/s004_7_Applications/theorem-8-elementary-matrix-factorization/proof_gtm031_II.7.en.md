---
role: proof
locale: en
of_concept: theorem-8-elementary-matrix-factorization
source_book: gtm031
source_chapter: "II"
source_section: "7"
---

We first observe that if $(f_1, f_2, \cdots, f_n)$ is an ordered basis of an $n$-dimensional (left) vector space over $\Delta$, then the following sets are also ordered bases:

1. $(f_1, \cdots, f_{p-1}, f_p', f_{p+1}, \cdots, f_n)$ where $f_p' = f_p + \beta f_q$, $q \neq p$.
2. $(f_1, \cdots, f_{p-1}, f_p', f_{p+1}, \cdots, f_n)$ where $f_p' = \gamma f_p$, $\gamma \neq 0$.
3. $(f_1, \cdots, f_{p-1}, f_p', f_{p+1}, \cdots, f_{q-1}, f_q', f_{q+1}, \cdots, f_n)$ where $f_p' = f_q$, $f_q' = f_p$.

Moreover, the matrices of these bases relative to the original basis $(f_1, \cdots, f_n)$ are elementary matrices of types I, II, or III respectively. These elementary matrices belong to $L(\Delta, n)$, with inverses:
$$T_{pq}(\beta)^{-1} = T_{pq}(-\beta), \quad D_p(\gamma)^{-1} = D_p(\gamma^{-1}), \quad P_{pq}^{-1} = P_{pq}.$$

Now let $(\alpha) \in L(\Delta, n)$ be arbitrary. Choose a basis $(e_1, \cdots, e_n)$ and define $f_i = \sum_j \alpha_{ij} e_j$. Since $(\alpha)$ is invertible, $(f_1, \cdots, f_n)$ is an ordered basis. We show by induction on $n$ that we can pass from $(f_1, \cdots, f_n)$ to $(e_1, \cdots, e_n)$ by a finite sequence of elementary replacements of the types above.

**Base case $n = 1$:** Trivial.

**Inductive step:** Assume the result for $(n-1)$-dimensional spaces. The $f_i$ cannot all lie in $[e_2, \cdots, e_n]$, so some $\alpha_{p1} \neq 0$. Interchange $f_1$ and $f_p$ (a type III operation) to obtain a basis $(f_1', f_2, \cdots)$ where $f_1'$ has non-zero $e_1$-coefficient.

Now use type I operations: replace $f_k$ ($k \geq 2$) by $f_k^* = f_k + \beta_k f_1'$ with $\beta_k$ chosen so that $f_k^* \in [e_2, \cdots, e_n]$. This yields a basis $(f_1', f_2^*, \cdots, f_n^*)$ where $f_2^*, \cdots, f_n^* \in [e_2, \cdots, e_n]$. These $n-1$ vectors are linearly independent, hence form a basis of $[e_2, \cdots, e_n]$.

By the induction hypothesis, we can pass by elementary replacements (involving only indices $2$ through $n$) from $(f_2^*, \cdots, f_n^*)$ to $(e_2, \cdots, e_n)$ while keeping $f_1'$ fixed. This gives the basis $(f_1', e_2, \cdots, e_n)$.

Finally, use type I operations to eliminate the $e_k$-coefficients ($k \geq 2$) from $f_1'$, obtaining $f_1'' = f_1' + \sum_{k=2}^n \mu_k e_k$ that involves only $e_1$. Then $f_1'' = \gamma e_1$ for some $\gamma \neq 0$. A type II operation multiplies by $\gamma^{-1}$ to yield $e_1$.

Thus $(e_1, \cdots, e_n)$ is reached by a finite sequence of elementary replacements. Each replacement corresponds to multiplying the matrix of the current basis by an elementary matrix. Therefore $(\alpha)^{-1}$, the matrix converting $(f_1, \cdots, f_n)$ to $(e_1, \cdots, e_n)$, is a product of elementary matrices. Since the inverse of an elementary matrix is again elementary, $(\alpha)$ itself is also a product of elementary matrices.
