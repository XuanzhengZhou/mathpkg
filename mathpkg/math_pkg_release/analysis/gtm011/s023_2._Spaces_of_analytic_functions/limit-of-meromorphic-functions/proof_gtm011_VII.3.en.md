---
role: proof
locale: en
of_concept: limit-of-meromorphic-functions
source_book: gtm011
source_chapter: "VII"
source_section: "3"
---

Suppose there exists a point $a \in G$ with $f(a) \neq \infty$. Set $M = |f(a)| + 1$. By Proposition 3.3(a), there exists $\rho > 0$ such that $B_\infty(f(a); \rho) \subset B(f(a); M)$. Since $f_n \to f$ uniformly on compact subsets of $G$ in the chordal metric, there exists a neighborhood $U$ of $a$ and an integer $N$ such that for $n \geq N$ and $z \in U$, $d(f_n(z), f(z)) < \rho$. In particular, for $n \geq N$ and $z \in U$, $f_n(z) \in B_\infty(f(z); \rho)$.

Now, since $f_n$ are analytic (the first case: each $f_n$ is meromorphic with finitely many poles), we can choose $U$ small enough so that none of the $f_n$ (for $n \geq N$) have poles in $U$. Then on $U$, the $f_n$ are analytic and uniformly bounded. By Theorem 2.1 (applied to the sequence $\{f_n\}_{n \geq N}$ on $U$), the limit $f$ is analytic on $U$.

This argument shows $f$ is analytic at every point of $G$ where $f$ is finite. The points where $f(z) = \infty$ are either poles (if $1/f$ has a zero there, making $f$ meromorphic) or accumulation points of poles where $f \equiv \infty$ in a neighborhood. The latter case forces $f \equiv \infty$ globally by the identity principle for meromorphic functions.

For the analytic case: if each $f_n$ is analytic, then by the first part $f$ is meromorphic. But an analytic function has no poles, so if $f \not\equiv \infty$, the limit must also be analytic. The only alternative is $f \equiv \infty$.
