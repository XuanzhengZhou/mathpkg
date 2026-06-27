---
role: proof
locale: en
of_concept: polynomial-nonzero-evaluation
source_book: gtm028
source_chapter: "II"
source_section: "18"
---

We proceed by induction on $n$. For $n=1$, this is Corollary 2 to Theorem 9 of §17: a non-zero polynomial in one variable over an integral domain has at most $\partial f$ roots, so on an infinite set $Q$, some evaluation is non-zero.

Assume the theorem true for $n-1$ indeterminates. Write $f$ as a polynomial in $X_n$ with coefficients in $R[X_1,\dots,X_{n-1}]$:
$$f(X_1,\dots,X_n) = \sum_{k=0}^{d} g_k(X_1,\dots,X_{n-1}) X_n^k,$$
where at least one $g_k$ is non-zero. By the induction hypothesis applied to $g_k$ (or the highest non-zero $g_k$), there exist $a_1,\dots,a_{n-1} \in Q$ such that $g_k(a_1,\dots,a_{n-1}) \neq 0$. Then $f(a_1,\dots,a_{n-1}, X_n)$ is a non-zero polynomial in the single variable $X_n$ with coefficients in $R$. Applying the $n=1$ case, there exists $a_n \in Q$ such that $f(a_1,\dots,a_n) \neq 0$. This completes the induction.
