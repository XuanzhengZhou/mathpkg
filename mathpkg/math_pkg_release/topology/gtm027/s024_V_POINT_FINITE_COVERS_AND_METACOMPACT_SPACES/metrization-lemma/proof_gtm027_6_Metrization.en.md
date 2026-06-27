---
role: proof
locale: en
of_concept: metrization-lemma
source_book: gtm027
source_chapter: "6"
source_section: "Metrization"
---

# Proof of the Metrization Lemma for Uniform Spaces (Lemma 6.12)

**Lemma 6.12 (Metrization Lemma).** Let $\{U_n : n \in \omega\}$ be a sequence of subsets of $X \times X$ such that $U_0 = X \times X$, each $U_n$ contains the diagonal, and $U_{n+1} \circ U_{n+1} \circ U_{n+1} \subset U_n$ for each $n$. Then there is a non-negative real-valued function $d$ on $X \times X$ such that

(a) $d(x,y) + d(y,z) \geq d(x,z)$ for all $x, y,$ and $z$; and

(b) $U_n \subset \{(x,y) : d(x,y) < 2^{-n}\} \subset U_{n-1}$ for each positive integer $n$.

If each $U_n$ is symmetric, then there is a pseudo-metric $d$ satisfying condition (b).

**Proof.** Define a real-valued function $f$ on $X \times X$ by letting $f(x,y) = 2^{-n}$ if $(x,y) \in U_{n-1} \setminus U_n$ and $f(x,y) = 0$ if $(x,y)$ belongs to every $U_n$.

For each $x$ and each $y$ in $X$, define $d(x,y)$ to be the infimum of $\sum \{f(x_i, x_{i+1}) : i = 0, \ldots, n\}$ over all finite chains $x = x_0, x_1, \ldots, x_{n+1} = y$.

The triangle inequality (a) follows directly from the definition by chaining.

For property (b), we show by induction on the length of a chain that if $\sum f(x_i, x_{i+1}) < 2^{-m}$, then $(x_0, x_{n+1}) \in U_m$.

Base case: a chain of length 1 is trivial.

Inductive step: consider a chain from $x_0$ to $x_{n+1}$ of total $f$-length $a$. Let $k$ be the largest integer such that the chain from $0$ to $k$ has $f$-length at most $a/2$, and notice that the chain from $k+1$ to $n+1$ also has $f$-length at most $a/2$. By the induction hypothesis, each of $f(x_0, x_k)$ and $f(x_{k+1}, x_{n+1})$ (in terms of the constructed $d$) is at most $2(a/2) = a$, and $f(x_k, x_{k+1}) \leq a$. If $m$ is the smallest integer such that $2^{-m} \leq a$, then $(x_0, x_k), (x_k, x_{k+1})$, and $(x_{k+1}, x_{n+1})$ all belong to $U_m$, and therefore $(x_0, x_{n+1}) \in U_{m-2}$ using the triple composition property (or $U_{m-1}$ if threefold composition is used).

This yields the desired bounds: $U_{n+2} \subset \{d < 2^{-n}\} \subset U_n$. By reindexing we obtain condition (b).

If each $U_n$ is symmetric, then $f$ is symmetric, and consequently $d$ is symmetric, making $d$ a pseudo-metric.
